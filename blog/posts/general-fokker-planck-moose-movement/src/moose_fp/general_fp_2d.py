"""A general Fokker-Planck model of moose movement in two dimensions.

This solves the Fokker-Planck equation

    dp/dt = -div[ b(x) p ] + d_i d_j [ D_ij(x) p ],

with a habitat potential U so that the drift is b = -grad U (plus an optional
nonlocal interaction term), a spatially varying diffusion D(x), and no-flux
walls around the domain and around a barrier (a river with a crossing).

Three experiments are reported:

1. equilibrium for a constant diffusion: p ~ exp(-U / D), including the effect
   of the barrier on how fast that equilibrium is approached;
2. the transient mixing of the two home-range lobes with and without the
   barrier;
3. a spatially varying diffusion, for which exp(-U / D) is no longer the
   stationary solution.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from moose_fp.numerics import total_variation

LENGTH = 4.0  # Domain side length, km
GRID = 81  # Cells per side
D0 = 0.5  # Base diffusion, km^2/h
DEPTH = 2.0  # Habitat well depth
WIDTH = 0.5  # Habitat well width, km


def build_domain(
    length: float = LENGTH,
    grid: int = GRID,
    depth: float = DEPTH,
    well_width: float = WIDTH,
):
    """Return ``(x, y, xx, yy, potential, solid)`` for the toy landscape.

    The landscape has two Gaussian habitat wells and a river at ``x = 2`` km
    with a single bridge near ``y = 0.7`` km. ``solid`` marks the cells that
    are walled off (the river outside the bridge).
    """
    x = np.linspace(0.0, length, grid)
    y = np.linspace(0.0, length, grid)
    xx, yy = np.meshgrid(x, y, indexing="ij")

    # Two home-range wells, one on each side of the river.
    wells = [(1.0, 2.0), (3.0, 2.0)]
    potential = np.zeros_like(xx)
    for wx, wy in wells:
        potential -= depth * np.exp(
            -((xx - wx) ** 2 + (yy - wy) ** 2) / (2 * well_width**2)
        )

    # A river at x = 2 with a single bridge at y ~ 0.7.
    solid = np.zeros_like(xx, dtype=bool)
    wall = np.isclose(xx, 2.0, atol=0.75 * (x[1] - x[0]))
    bridge = np.abs(yy - 0.7) < 0.2
    solid[wall & ~bridge] = True

    return x, y, xx, yy, potential, solid


def steady_state(potential, solid, diffusion, weights=None):
    """Boltzmann prediction p ~ exp(-U / D) on the open cells."""
    if weights is None:
        weights = np.ones_like(potential)
    p = np.where(solid, 0.0, weights * np.exp(-potential / diffusion))
    p /= p.sum()
    return p


def gradient(field, spacing):
    """Central gradient with second-order edges."""
    return np.gradient(field, spacing, edge_order=2)


def solve(
    potential,
    solid,
    diffusion,
    p0,
    t_end,
    interaction=0.0,
    record_times=(),
):
    """Explicit finite-volume integration of the general Fokker-Planck equation.

    ``diffusion`` may be a scalar or a two-dimensional array. ``interaction``
    is the strength of a nonlocal attraction towards the mean of the
    distribution (McKean-Vlasov term); zero means no interaction.

    Returns ``(p, dt, saved, open_)`` where ``saved`` maps each requested
    record time to a copy of the density at that time.
    """
    nx, ny = potential.shape
    dx = LENGTH / (nx - 1)
    dy = LENGTH / (ny - 1)

    if np.isscalar(diffusion):
        diffusion = np.full_like(potential, diffusion)

    bx, by = gradient(-potential, dx)

    d_max = float(np.max(diffusion[~solid]))
    b_max = max(float(np.max(np.abs(bx[~solid]))), float(np.max(np.abs(by[~solid]))))
    # 2D explicit stability: diffusion number D dt / dx^2 <= 1/4 and
    # advective CFL |b| dt / dx <= 1, with a safety factor.
    dt = 0.2 * min(dx**2 / d_max, dx / max(b_max, 1e-12))
    n_steps = round(t_end / dt)

    p = np.zeros_like(potential)
    p[:] = p0
    p[solid] = 0.0

    open_ = ~solid
    saved = {}
    next_record = 0

    for step in range(n_steps):
        drift_x, drift_y = bx, by
        if interaction != 0.0:
            smoothed = smooth(p)
            gx, gy = gradient(smoothed, dx)
            drift_x = bx - interaction * gx
            drift_y = by - interaction * gy

        flux_x = face_flux(p, drift_x, diffusion, solid, axis=0, spacing=dx)
        flux_y = face_flux(p, drift_y, diffusion, solid, axis=1, spacing=dy)

        divergence = divergence_from_flux(flux_x, flux_y, spacing=dx)
        p = p - dt * divergence
        p[solid] = 0.0
        p[p < 0.0] = 0.0

        if next_record < len(record_times) and (step + 1) * dt >= record_times[next_record]:
            saved[record_times[next_record]] = p.copy()
            next_record += 1

    return p, dt, saved, open_


def face_flux(p, drift, diffusion, solid, axis, spacing):
    """Advective (upwinded) plus diffusive flux on the cell faces."""
    if axis == 0:
        solid_face = solid[:-1, :] | solid[1:, :]
        drift_face = 0.5 * (drift[:-1, :] + drift[1:, :])
        diff_face = 0.5 * (diffusion[:-1, :] + diffusion[1:, :])
        left, right = p[:-1, :], p[1:, :]
    else:
        solid_face = solid[:, :-1] | solid[:, 1:]
        drift_face = 0.5 * (drift[:, :-1] + drift[:, 1:])
        diff_face = 0.5 * (diffusion[:, :-1] + diffusion[:, 1:])
        left, right = p[:, :-1], p[:, 1:]

    upwind = np.where(drift_face > 0, left, right)
    flux = drift_face * upwind - diff_face * (right - left) / spacing
    return np.where(solid_face, 0.0, flux)


def divergence_from_flux(flux_x, flux_y, spacing):
    """Divergence of a face-centred flux on a cell-centred grid."""
    nx, ny = flux_x.shape[0] + 1, flux_x.shape[1]
    divergence = np.zeros((nx, ny))

    face_x = np.zeros((nx + 1, ny))
    face_x[1:-1] = flux_x
    divergence += (face_x[1:] - face_x[:-1]) / spacing

    face_y = np.zeros((nx, ny + 1))
    face_y[:, 1:-1] = flux_y
    divergence += (face_y[:, 1:] - face_y[:, :-1]) / spacing

    return divergence


def smooth(field):
    """Small Gaussian smoothing used for the nonlocal interaction term."""
    from scipy.ndimage import gaussian_filter

    return gaussian_filter(field, sigma=2.0, mode="nearest")


def centre_delta(x, y, cx, cy, solid):
    """A point mass at the grid node nearest ``(cx, cy)``, normalised."""
    p = np.zeros((len(x), len(y)))
    i = int(np.argmin(np.abs(x - cx)))
    j = int(np.argmin(np.abs(y - cy)))
    p[i, j] = 1.0
    p[solid] = 0.0
    return p / p.sum()


def _plot(xx, yy, potential, solid, equilibrium, record_times, error_barrier,
          error_free, open_cells, p_variable, diffusion_field):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10.5))
    extent = [0, LENGTH, 0, LENGTH]

    ax = axes[0, 0]
    image = ax.imshow(potential.T, origin="lower", extent=extent, cmap="terrain")
    ax.contour(xx.T, yy.T, potential.T, levels=8, colors="black", linewidths=0.4)
    ax.imshow(
        np.where(solid, 1.0, np.nan).T,
        origin="lower",
        extent=extent,
        cmap="Greys",
        vmin=0,
        vmax=1,
        alpha=0.9,
    )
    ax.set_title("Habitat potential U (dark = good) and river with bridge")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    fig.colorbar(image, ax=ax, label="U")

    ax = axes[0, 1]
    image = ax.imshow(equilibrium.T, origin="lower", extent=extent, cmap="viridis")
    ax.set_title(r"Equilibrium for constant $D$: $p \propto e^{-U/D}$")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    fig.colorbar(image, ax=ax, label="density")

    ax = axes[1, 0]
    ax.plot(record_times, error_barrier, color="darkred", linewidth=2, label="with river")
    ax.plot(record_times, error_free, color="steelblue", linewidth=2, label="no river")
    ax.set_yscale("log")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("total-variation distance to equilibrium")
    ax.set_title("The river slows mixing but not the equilibrium")
    ax.legend()

    ax = axes[1, 1]
    scatter = ax.scatter(
        -potential[open_cells] / D0,
        np.log(p_variable[open_cells]),
        c=np.log10(diffusion_field[open_cells]),
        s=12,
        cmap="plasma",
    )
    fit = np.polyfit(-potential[open_cells] / D0, np.log(p_variable[open_cells]), 1)
    xs = np.linspace(
        (-potential[open_cells] / D0).min(), (-potential[open_cells] / D0).max(), 10
    )
    ax.plot(xs, np.polyval(fit, xs), color="black", linewidth=2, label=f"slope {fit[0]:.2f}")
    ax.set_xlabel(r"$-U/D_0$")
    ax.set_ylabel(r"$\log p$ (steady state)")
    ax.set_title("Variable diffusion breaks the Boltzmann law")
    ax.legend()
    fig.colorbar(scatter, ax=ax, label=r"$\log_{10} D$")

    fig.suptitle("General Fokker-Planck model of moose movement")
    fig.tight_layout()
    return fig


def run(output: str | Path = "figures/general_fp_2d.png") -> Path:
    """Run the three experiments, print diagnostics, and write the figure."""
    x, y, xx, yy, potential, solid = build_domain()

    equilibrium = steady_state(potential, solid, D0)

    # --- Experiment 1 and 2: barrier versus no barrier -------------------
    record_times = np.linspace(0.0, 60.0, 121)
    start = centre_delta(x, y, 1.0, 2.0, solid)

    _p_barrier, _dt, saved_barrier, _ = solve(
        potential, solid, D0, start, 60.0, record_times=tuple(record_times)
    )
    p_free, _, saved_free, _ = solve(
        potential, np.zeros_like(solid), D0, start, 60.0, record_times=tuple(record_times)
    )

    error_barrier = np.array(
        [total_variation(saved_barrier[t], equilibrium) for t in record_times]
    )
    error_free = np.array([total_variation(saved_free[t], equilibrium) for t in record_times])

    # --- Experiment 3: spatially varying diffusion -----------------------
    diffusion_field = D0 * (1.0 + 0.9 * np.exp(-((xx - 3.0) ** 2 + (yy - 1.0) ** 2) / 1.5))
    p_variable, _, _, _ = solve(potential, solid, diffusion_field, start, 120.0)
    prediction = steady_state(potential, solid, D0)

    open_cells = ~solid & (prediction > 1e-5)
    ratios = p_variable[open_cells] / prediction[open_cells]

    print("\nBarrier delays mixing:")
    for t in (2.0, 5.0, 10.0, 20.0, 40.0, 60.0):
        k = int(np.argmin(np.abs(record_times - t)))
        print(
            f"  t = {record_times[k]:5.1f} h"
            f"   TV to equilibrium: barrier {error_barrier[k]:.4f}"
            f"   no barrier {error_free[k]:.4f}"
        )

    max_rel_err = float(
        np.max(
            np.abs(
                p_free[open_cells] / p_free.sum() - equilibrium[open_cells] / equilibrium.sum()
            )
            / equilibrium[open_cells]
        )
    )

    corr = float(
        np.corrcoef(np.log(p_variable[open_cells]), -potential[open_cells] / D0)[0, 1]
    )

    print("\nSolver validation (constant D, no barrier):")
    print(f"  max relative error versus exp(-U/D): {max_rel_err:.4f}")
    print(f"  TV distance at t = 60 h:             {error_free[-1]:.5f}")

    print("\nVariable diffusion versus the constant-D Boltzmann prediction:")
    print(f"  median ratio p_steady / (exp(-U/D0) normalised): {np.median(ratios):.3f}")
    print(
        f"  interquartile range of ratio:                    "
        f"{np.subtract(*np.percentile(ratios, [75, 25])):.3f}"
    )
    print(f"  correlation of log p with -U/D0:                 {corr:.3f}")

    fig = _plot(
        xx,
        yy,
        potential,
        solid,
        equilibrium,
        record_times,
        error_barrier,
        error_free,
        open_cells,
        p_variable,
        diffusion_field,
    )

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point."""
    run()


if __name__ == "__main__":
    main()
