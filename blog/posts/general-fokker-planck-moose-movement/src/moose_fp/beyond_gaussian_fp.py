"""Three ways of repairing the Ornstein-Uhlenbeck model of moose movement.

1. Fractional diffusion: replace the Laplacian by the fractional Laplacian of
   order 2 alpha, so the Fokker-Planck operator becomes
       dp/dt = -d/dx (b p) + D (-d^2/dx^2)^alpha p ,
   and the stationary density acquires power-law tails instead of decaying
   like a Gaussian. Solved with a split scheme: the exact Ornstein-Uhlenbeck
   contraction, remapped conservatively cell by cell, then exact fractional
   diffusion applied in Fourier space.

2. Nonlocal interaction: add a McKean-Vlasov drift that pulls each animal
   towards the local density of animals, in the form
       b(x) = -kappa x + chi d/dx log(G * p) .
   Solved with the explicit finite-volume scheme until it stops changing.

3. Behavioural states: two coupled Fokker-Planck equations for a moose that
   switches between a tight core range and a wider exploratory mode.
       dp_i/dt = -d/dx (b_i p_i) + D_i d^2p_i/dx^2 + q_ji p_j - q_ij p_i
   Solved in time from a point mass, then compared against a single-state
   Ornstein-Uhlenbeck fit.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

from moose_fp.numerics import total_variation

ALPHA = 0.5  # Fractional order of the diffusion operator / 2
KAPPA = 1.0  # OU fidelity, 1/h
DIFFUSION = 1.0  # Diffusion coefficient, km^2/h


def flow_contract(p, x, a):
    """Push cell masses through the exact OU contraction x -> x/a.

    The Ornstein-Uhlenbeck drift -kappa x points inward everywhere, so the
    deterministic flow of one step maps the domain into itself without any
    wraparound: mass in the outer strips moves in and leaves a hole near the
    seam, which the diffusion step then refills. The remap reads mass off the
    cumulative distribution and conserves it exactly.
    """
    nodes = np.append(x, x[-1] + (x[1] - x[0]))
    cumulative = np.concatenate(([0.0], np.cumsum(p)))
    preimages = np.clip(a * nodes, nodes[0], nodes[-1])
    moved = np.interp(preimages, nodes, cumulative)
    return moved[1:] - moved[:-1]


def fractional_ou(alpha, n_steps, dt, grid, length):
    """Stationary density of the fractional OU process on a periodic domain.

    Returns ``(x, p, spacing, mass_drift)`` where ``p`` is normalised as a
    density and ``mass_drift`` is the largest deviation from total mass one
    seen over the run.
    """
    x = -0.5 * length + np.arange(grid) * (length / grid)
    spacing = length / grid
    k = 2.0 * np.pi * np.fft.fftfreq(grid, d=spacing)

    p = np.exp(-0.5 * KAPPA * x**2)
    p /= p.sum()

    contraction = np.exp(KAPPA * dt)
    evolved = np.exp(-DIFFUSION * np.abs(k) ** (2.0 * alpha) * dt)

    low = high = p.sum()
    for _ in range(n_steps):
        p = flow_contract(p, x, contraction)
        p = np.real(np.fft.ifft(np.fft.fft(p) * evolved))
        low = min(low, p.sum())
        high = max(high, p.sum())

    p = p / (p.sum() * spacing)
    return x, p, spacing, high - low


def advance_periodic(p, drift, spacing, diffusion, dt):
    """Conservative explicit step for dp/dt = -d/dx (b p) + d^2 (D p)/dx^2."""
    b_face = 0.5 * (drift + np.roll(drift, -1))
    upwind = np.where(b_face > 0.0, p, np.roll(p, -1))
    flux = upwind * b_face - diffusion * (np.roll(p, -1) - p) / spacing
    p = p - dt * (flux - np.roll(flux, 1)) / spacing
    return np.maximum(p, 0.0)


def drift_habitat(x):
    """The Ornstein-Uhlenbeck restoring drift -kappa x."""
    return -KAPPA * x


def interaction_run(chi, grid, length, dt, t_end, width, tolerance=1e-10):
    """Equilibrium with a nonlocal attraction towards the animal density.

    Returns ``(x, p, elapsed_time, final_change)``.
    """
    x = -0.5 * length + np.arange(grid) * (length / grid)
    spacing = length / grid

    p = np.exp(-0.5 * KAPPA * x**2)
    p /= p.sum()

    n_steps = round(t_end / dt)
    previous = p.copy()
    change = float("nan")
    for step in range(n_steps):
        drift = drift_habitat(x)
        if chi != 0.0:
            smoothed = gaussian_filter1d(p, sigma=width / spacing, mode="nearest")
            smoothed = np.maximum(smoothed, 1e-14 * smoothed.max())
            drift = drift + chi * np.gradient(np.log(smoothed), spacing)
        p = advance_periodic(p, drift, spacing, DIFFUSION, dt)
        if step % 200 == 0 and step > 0:
            change = 0.5 * np.sum(np.abs(p - previous))
            if change < tolerance:
                return x, p, (step + 1) * dt, change
            previous = p.copy()

    return x, p, n_steps * dt, change


def self_consistent_variance(chi, width, iterations=400):
    """Fixed point of v = D / (kappa + chi / (v + width^2)) for a Gaussian."""
    variance = DIFFUSION / KAPPA
    for _ in range(iterations):
        variance = DIFFUSION / (KAPPA + chi / (variance + width**2))
    return variance


def face_flux(p, drift, spacing, diffusion):
    """Advective (upwinded) plus diffusive flux on the cell faces."""
    flux = np.zeros(len(p) + 1)
    interior_b = 0.5 * (drift[:-1] + drift[1:])
    interior = (
        np.where(interior_b > 0.0, p[:-1], p[1:]) * interior_b
        - diffusion * (p[1:] - p[:-1]) / spacing
    )
    flux[1:-1] = interior
    return flux


def switch_run(x, spacing, dt, t_end, snapshot_at):
    """Time-dependent solution of the two coupled state equations.

    Returns a dict mapping each requested snapshot time to ``(p_a, p_b)``.
    """
    state_a = {"kappa": 1.0, "centre": -3.0, "diffusion": 0.25, "out": 0.10}
    state_b = {"kappa": 0.5, "centre": 2.5, "diffusion": 0.60, "out": 0.10}

    p_a = np.where(np.isclose(x, -3.0), 1.0, 0.0)
    p_b = np.zeros_like(p_a)
    p_a /= p_a.sum()

    n_steps = round(t_end / dt)
    snapshots = {}
    for step in range(n_steps):
        flux_a = face_flux(
            p_a, -state_a["kappa"] * (x - state_a["centre"]), spacing, state_a["diffusion"]
        )
        flux_b = face_flux(
            p_b, -state_b["kappa"] * (x - state_b["centre"]), spacing, state_b["diffusion"]
        )

        p_a_next = p_a - dt * (flux_a[1:] - flux_a[:-1]) / spacing
        p_b_next = p_b - dt * (flux_b[1:] - flux_b[:-1]) / spacing

        p_a_next += dt * (-state_a["out"] * p_a + state_b["out"] * p_b)
        p_b_next += dt * (-state_b["out"] * p_b + state_a["out"] * p_a)

        p_a = np.maximum(p_a_next, 0.0)
        p_b = np.maximum(p_b_next, 0.0)

        for when in snapshot_at:
            if abs((step + 1) * dt - when) < 0.5 * dt:
                snapshots[when] = (p_a.copy(), p_b.copy())

    return snapshots


def sample_path(grid_dt, t_end, seed=20261016):
    """One representative animal path with switching behaviour.

    Returns ``(times, position, states)``.
    """
    rng = np.random.default_rng(seed)
    n = round(t_end / grid_dt)
    times = np.arange(n + 1) * grid_dt

    states = np.zeros(n + 1, dtype=int)
    position = np.zeros(n + 1)
    for i in range(n):
        states[i + 1] = states[i]
        if rng.random() < 0.10 * grid_dt:
            states[i + 1] = 1 - states[i]

        current = states[i + 1]
        kappa, centre, diffusion = [
            (1.0, -3.0, 0.25),
            (0.5, 2.5, 0.60),
        ][current]
        drift = -kappa * (position[i] - centre)
        position[i + 1] = (
            position[i] + drift * grid_dt + np.sqrt(2.0 * diffusion * grid_dt) * rng.normal()
        )
    return times, position, states


def _plot(x_f, p_alpha1, p_alphahalf, gaussian, slope, intercept, x_i, p_free,
          p_inter, x_s, mixture, p_a, p_b, gaussian_fit, times, path):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    ax = axes[0, 0]
    core = (x_f > 0.4) & (x_f < 10.0) & (p_alpha1 > 1e-12)
    ax.loglog(x_f[core], p_alpha1[core], color="steelblue", linewidth=2,
              label=r"$\alpha = 1$ (Gaussian)")
    ax.loglog(x_f[core], gaussian[core], color="black", linestyle="--", linewidth=1.5,
              label="exact Gaussian")
    tail_alpha = (x_f > 0.4) & (x_f < 10.0) & (p_alphahalf > 1e-14)
    ax.loglog(x_f[tail_alpha], p_alphahalf[tail_alpha], color="darkred", linewidth=2,
              label=r"$\alpha = 0.5$")
    reference = np.exp(intercept) * (x_f[tail_alpha] ** slope)
    ax.loglog(x_f[tail_alpha], reference, color="darkorange", linestyle=":", linewidth=1.5,
              label=f"tail slope {slope:.2f}")
    ax.set_xlabel("distance from home range centre (km)")
    ax.set_ylabel("stationary density")
    ax.set_title("Fractional diffusion gives power-law tails")
    ax.legend(fontsize=9)

    ax = axes[0, 1]
    ax.plot(x_i, p_free, color="steelblue", linewidth=2,
            label=r"$\chi = 0$ (independent moose)")
    ax.plot(x_i, p_inter, color="darkred", linewidth=2,
            label=r"$\chi = 0.6$ (nonlocal attraction)")
    ax.set_xlabel("distance from home range centre (km)")
    ax.set_ylabel("stationary density")
    ax.set_title("Interaction makes the herd bunch together")
    ax.legend(fontsize=9)

    ax = axes[1, 0]
    ax.fill_between(x_s, mixture, color="grey", alpha=0.35, label="total density")
    ax.plot(x_s, p_a, color="steelblue", linewidth=2, label="state A: core range")
    ax.plot(x_s, p_b, color="darkred", linewidth=2, label="state B: exploratory")
    ax.plot(x_s, gaussian_fit, color="black", linestyle="--", linewidth=1.5,
            label="single-state fit")
    ax.set_xlabel("distance from home range centre (km)")
    ax.set_ylabel("stationary density")
    ax.set_title("Behavioural states turn one Gaussian into two lobes")
    ax.legend(fontsize=9)

    ax = axes[1, 1]
    for _mode, colour, label in ((0, "steelblue", "state A"), (1, "darkred", "state B")):
        ax.scatter(times, path, s=2.5, color=colour, label=label, rasterized=True)
    ax.set_xlabel("t (h)")
    ax.set_ylabel("position (km)")
    ax.set_title("One animal switching between behaviours")
    ax.legend(fontsize=9, markerscale=3)

    fig.suptitle("Beyond the Ornstein-Uhlenbeck model")
    fig.tight_layout()
    return fig


def run(output: str | Path = "figures/beyond_gaussian_fp.png") -> Path:
    """Run the three one-dimensional repairs, print diagnostics, write figure."""
    # --- Fractional tails ------------------------------------------------
    x_f, p_alpha1, spacing_f, _mass_alpha1 = fractional_ou(
        alpha=1.0, n_steps=20000, dt=0.005, grid=2048, length=32.0
    )
    x_f, p_alphahalf, _, _mass_alphahalf = fractional_ou(
        alpha=ALPHA, n_steps=20000, dt=0.005, grid=2048, length=32.0
    )

    gaussian = KAPPA * np.exp(-0.5 * KAPPA * x_f**2) / np.sqrt(2.0 * np.pi * DIFFUSION)
    tv_alpha1 = total_variation(p_alpha1, gaussian, spacing_f)

    tail = (x_f > 2.5) & (x_f < 6.0) & (p_alphahalf > 1e-14)
    slope, intercept = np.polyfit(np.log(x_f[tail]), np.log(p_alphahalf[tail]), 1)

    print("Fractional OU, 20000 split steps of 0.005 h, 2048 points on [-16, 16) km")
    print(f"  alpha = 1:   mass drift over the run {_mass_alpha1:.3e}")
    print(f"  alpha = 0.5: mass drift over the run {_mass_alphahalf:.3e}")
    print(f"  alpha = 1 TV distance to the exact Gaussian: {tv_alpha1:.4f}")
    print(f"  alpha = 0.5 tail fit on 2.5-6 km: slope {slope:.3f} (predicted -2.000)")

    # --- Nonlocal interaction -------------------------------------------
    width = 0.5
    interaction_grid = 256
    interaction_spacing = 16.0 / interaction_grid
    dt = 0.2 * interaction_spacing**2 / DIFFUSION
    x_i, p_free, t_free, change_free = interaction_run(
        0.0, interaction_grid, 16.0, dt, 400.0, width
    )
    x_i, p_inter, t_inter, change_inter = interaction_run(
        0.6, interaction_grid, 16.0, dt, 400.0, width
    )

    def variance(p):
        mean = float(np.sum(p * x_i))
        return float(np.sum(p * x_i**2)) - mean**2

    v_free, v_inter = variance(p_free), variance(p_inter)
    v_predicted = self_consistent_variance(0.6, width)
    gaussian_predicted = np.exp(-0.5 * x_i**2 / v_predicted)
    gaussian_predicted /= gaussian_predicted.sum()
    tv_prediction = total_variation(p_inter, gaussian_predicted)
    tv_equilibria = total_variation(p_inter, p_free)

    print(f"\nNonlocal attraction chi = 0.6 km^2/h, interaction width {width} km")
    print(f"  converged after {t_free:.1f} h (chi = 0) and {t_inter:.1f} h (chi = 0.6)")
    print(f"  final TV change: {change_free:.2e} and {change_inter:.2e}")
    print(f"  variance: no interaction {v_free:.3f}, with interaction {v_inter:.3f}")
    print(f"  self-consistent Gaussian prediction: {v_predicted:.3f}")
    print(f"  TV distance from that prediction: {tv_prediction:.3f}")
    print(f"  TV distance between the two equilibria: {tv_equilibria:.3f}")

    # --- Behavioural states ----------------------------------------------
    grid_s, length_s = 384, 16.0
    spacing_s = length_s / grid_s
    x_s = -0.5 * length_s + np.arange(grid_s) * spacing_s
    dt_s = 0.25 * spacing_s**2 / 0.60

    snapshots = switch_run(x_s, spacing_s, dt_s, 100.0, snapshot_at=(60.0, 100.0))
    p_a, p_b = snapshots[100.0]
    mixture = p_a + p_b

    mean = float(np.sum(mixture * x_s))
    sd = float(np.sqrt(np.sum(mixture * (x_s - mean) ** 2)))
    gaussian_fit = np.exp(-0.5 * ((x_s - mean) / sd) ** 2)
    gaussian_fit /= gaussian_fit.sum()

    tv_gaussian = total_variation(mixture, gaussian_fit)
    tv_stationary = total_variation(
        snapshots[60.0][0] + snapshots[60.0][1], mixture
    )
    midpoint_ratio = float(mixture[np.isclose(x_s, 0.0)][0]) / float(np.max(mixture))

    print("\nTwo behavioural states, 100 h of switching (10 h typical per state)")
    print(f"  mass in state A {np.sum(p_a):.6f}, state B {np.sum(p_b):.6f}")
    print(f"  change between t = 60 h and t = 100 h: TV {tv_stationary:.2e}")
    print(f"  mixture mean {mean:.3f} km, sd {sd:.3f} km")
    print(f"  TV distance from a single Gaussian with the same mean and sd: {tv_gaussian:.3f}")
    print(f"  density at the midpoint versus the highest mode: {midpoint_ratio:.3f}")

    times, path, _states = sample_path(0.005, 100.0)
    fraction_wide = float(np.mean(_states == 1))
    print(f"  example path: {fraction_wide:.3f} of the time in the wide mode")

    # --- Figure ----------------------------------------------------------
    fig = _plot(
        x_f,
        p_alpha1,
        p_alphahalf,
        gaussian,
        slope,
        intercept,
        x_i,
        p_free,
        p_inter,
        x_s,
        mixture,
        p_a,
        p_b,
        gaussian_fit,
        times,
        path,
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
