"""Fokker-Planck and analytic solutions of the Ornstein-Uhlenbeck moose model.

The companion Rust crate ``moose_ou`` simulates virtual moose whose positions
follow an Ornstein-Uhlenbeck (OU) process, that is, the It^o SDE

    dx = -kappa (x - c) dt + sigma dW

The density of those positions, p(x, t), obeys the Fokker-Planck equation

    dp/dt = kappa d/dx[(x - c) p] + (sigma^2 / 2) d^2p/dx^2.

This module solves that PDE directly on a grid with an explicit finite-volume
scheme (upwinded drift, centred diffusion, no-flux walls), and plots the PDE
solution against the simulated moose and against the analytic OU transition
density,

    X_t ~ Normal(c, (sigma^2 / 2 kappa) (1 - exp(-2 kappa t))).

Run the Rust crate first so that ``data/moose_positions.csv`` and
``data/moose_track.csv`` exist.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

KAPPA = 0.5
"""Home-range fidelity, in 1/h."""

SIGMA = 1.0
"""Exploratory jitter, in km/sqrt(h)."""

T_END = 20.0
"""Simulation length, in h."""

CENTRE = 0.0
"""Home-range centre, in km."""


def load_positions(path: str | Path) -> tuple[np.ndarray, np.ndarray]:
    """Load the final ``(x, y)`` positions of every moose from ``path``."""
    data = np.loadtxt(path, delimiter=",", skiprows=1)
    return data[:, 0], data[:, 1]


def load_track(path: str | Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Load a representative ``(t, x, y)`` trajectory from ``path``."""
    data = np.loadtxt(path, delimiter=",", skiprows=1)
    return data[:, 0], data[:, 1], data[:, 2]


def analytic_variance(t: float, *, kappa: float = KAPPA, sigma: float = SIGMA) -> float:
    """Variance of the OU process started at the centre.

    The variance relaxes from zero towards ``sigma**2 / (2 kappa)`` like
    ``1 - exp(-2 kappa t)``.
    """
    return sigma**2 / (2 * kappa) * (1 - np.exp(-2 * kappa * t))


def stationary_sd(*, kappa: float = KAPPA, sigma: float = SIGMA) -> float:
    """Stationary standard deviation per axis, ``sigma / sqrt(2 kappa)``."""
    return sigma / math.sqrt(2 * kappa)


def analytic_pdf(
    x: np.ndarray,
    t: float,
    *,
    kappa: float = KAPPA,
    sigma: float = SIGMA,
    centre: float = CENTRE,
) -> np.ndarray:
    """Transition density of the OU process at time ``t``."""
    variance = analytic_variance(t, kappa=kappa, sigma=sigma)
    return np.exp(-0.5 * (x - centre) ** 2 / variance) / math.sqrt(
        2 * math.pi * variance
    )


def solve_fokker_planck(
    extent: float = 5.0,
    dx: float = 0.01,
    dt: float = 5e-5,
    *,
    kappa: float = KAPPA,
    sigma: float = SIGMA,
    t_end: float = T_END,
    centre: float = CENTRE,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Finite-volume solution of the 1D Fokker-Planck equation.

    The probability current is written in flux form,

        J = -kappa (x - c) p - (sigma^2 / 2) dp/dx,

    with the advective part upwinded and the diffusive part centred, and the
    time step is explicit. The flux is set to zero at the two walls, so mass
    is conserved exactly. Upwinding adds a small numerical diffusion of size
    ``|v| dx / 2``, which is the main discretization error.

    Returns ``(x, times, snapshots, masses, means, variances)``.
    """
    x = np.arange(-extent, extent + dx / 2, dx)
    n_steps = round(t_end / dt)
    record_every = max(1, n_steps // 400)

    p = np.zeros_like(x)
    p[np.argmin(np.abs(x - centre))] = 1.0 / dx  # Start as a point mass

    diffusivity = sigma**2 / 2

    def step(density: np.ndarray) -> np.ndarray:
        # Probability current at the interior cell faces.
        velocity_face = -kappa * (0.5 * (x[:-1] + x[1:]) - centre)
        upwind = np.where(velocity_face > 0, density[:-1], density[1:])
        advective = velocity_face * upwind
        diffusive = -diffusivity * (density[1:] - density[:-1]) / dx

        # No-flux walls, so the interior update telescopes to zero.
        current = np.concatenate(([0.0], advective + diffusive, [0.0]))
        return density - dt / dx * (current[1:] - current[:-1])

    times = [0.0]
    snapshots = [p.copy()]
    masses = [float(np.sum(p) * dx)]
    means = [float(np.sum(x * p) * dx)]
    variances = [float(np.sum((x - centre) ** 2 * p) * dx)]

    for step_index in range(n_steps):
        p = step(p)

        if (step_index + 1) % record_every == 0:
            times.append((step_index + 1) * dt)
            snapshots.append(p.copy())
            masses.append(float(np.sum(p) * dx))
            means.append(float(np.sum(x * p) * dx))
            variances.append(float(np.sum((x - centre) ** 2 * p) * dx))

    return (
        x,
        np.array(times),
        np.array(snapshots),
        np.array(masses),
        np.array(means),
        np.array(variances),
    )


def diagnostics(
    masses: np.ndarray,
    means: np.ndarray,
    variances: np.ndarray,
    *,
    kappa: float = KAPPA,
    sigma: float = SIGMA,
    t_end: float = T_END,
    centre: float = CENTRE,
) -> dict[str, float]:
    """Compare the PDE solution at ``t_end`` with the analytic values."""
    return {
        "mass": float(masses[-1]),
        "pde_variance": float(variances[-1]),
        "analytic_variance": float(analytic_variance(t_end, kappa=kappa, sigma=sigma)),
        "pde_mean": float(means[-1]),
        "analytic_mean": float(centre),
    }


def print_diagnostics(diag: dict[str, float]) -> None:
    """Print the PDE-versus-analytic comparison quoted in the blog post."""
    print("Fokker-Planck PDE versus analytic solution:")
    print(f"  {'mass at T:':<20}{diag['mass']:.6f} (should be 1.000000)")
    print(f"  {'PDE variance at T:':<20}{diag['pde_variance']:.6f}")
    print(f"  {'analytic variance:':<20}{diag['analytic_variance']:.6f}")
    print(f"  {'PDE mean at T:':<20}{diag['pde_mean']:.6f}")
    print(f"  {'analytic mean:':<20}{diag['analytic_mean']:.6f}")


def plot_comparison(
    x_positions: np.ndarray,
    y_positions: np.ndarray,
    t_track: np.ndarray,
    x_track: np.ndarray,
    y_track: np.ndarray,
    solve: tuple[
        np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray
    ],
    output: str | Path,
    *,
    kappa: float = KAPPA,
    sigma: float = SIGMA,
    t_end: float = T_END,
    centre: float = CENTRE,
) -> Path:
    """Render the four-panel comparison figure and return the written path."""
    x, times, snapshots, _masses, _means, variances = solve

    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # (a) One simulated moose trajectory.
    ax = axes[0, 0]
    points = ax.scatter(x_track, y_track, c=t_track, cmap="viridis", s=6)
    ax.scatter([centre], [centre], marker="+", color="black", s=150, linewidths=2)
    ax.annotate(
        "home-range\ncentre",
        (centre, centre),
        xytext=(10, -25),
        textcoords="offset points",
        fontsize=9,
    )
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.set_title("One simulated moose, coloured by time (h)")
    fig.colorbar(points, ax=ax, label="t (h)")

    # (b) Final positions of all virtual moose against the analytic density.
    ax = axes[0, 1]
    ax.scatter(x_positions, y_positions, s=3, alpha=0.25, color="steelblue")
    radius = np.linspace(0, 2 * math.pi, 200)
    sd = stationary_sd(kappa=kappa, sigma=sigma)
    for level in (1, 2):
        ax.plot(
            level * sd * np.cos(radius),
            level * sd * np.sin(radius),
            color="darkred",
            linewidth=2,
        )
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.set_title("Final positions with 1 and 2 sd analytic contours")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

    # (c) 1D marginal: particles, Fokker-Planck PDE, and the analytic density.
    ax = axes[1, 0]
    bins = np.linspace(-4, 4, 41)
    ax.hist(
        x_positions,
        bins=bins,
        density=True,
        color="steelblue",
        alpha=0.6,
        label="simulated moose",
    )
    x_fine = np.linspace(-4, 4, 400)
    ax.plot(
        x_fine,
        analytic_pdf(x_fine, t_end, kappa=kappa, sigma=sigma, centre=centre),
        color="black",
        linewidth=2,
        label="analytic density at t = T",
    )
    ax.plot(
        x,
        snapshots[-1],
        color="darkred",
        linestyle="--",
        linewidth=2,
        label="Fokker-Planck PDE",
    )
    ax.set_xlabel("x (km)")
    ax.set_ylabel("density (1/km)")
    ax.set_title(f"Marginal distribution at t = {t_end:.0f} h")
    ax.legend(fontsize=9)

    # (d) Relaxation of the variance towards its equilibrium value.
    ax = axes[1, 1]
    ax.plot(
        times,
        variances,
        color="darkred",
        linestyle="--",
        label="Fokker-Planck PDE",
    )
    t_fine = np.linspace(0, t_end, 300)
    ax.plot(
        t_fine,
        analytic_variance(t_fine, kappa=kappa, sigma=sigma),
        color="black",
        linewidth=2,
        label="analytic",
    )
    ax.axhline(sigma**2 / (2 * kappa), color="grey", linewidth=1, label="equilibrium")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("variance (km$^2$)")
    ax.set_title("Relaxation of the density to equilibrium")
    ax.legend(fontsize=9)

    fig.suptitle(
        "Ornstein-Uhlenbeck moose movement: particles versus the Fokker-Planck equation",
    )
    fig.tight_layout()

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return output_path


def run(
    positions_path: str | Path = "data/moose_positions.csv",
    track_path: str | Path = "data/moose_track.csv",
    output: str | Path = "figures/moose_fokker_planck.png",
) -> Path:
    """Solve, compare, plot, and print diagnostics for the OU moose model."""
    x_positions, y_positions = load_positions(positions_path)
    t_track, x_track, y_track = load_track(track_path)

    solve = solve_fokker_planck()
    _x, _times, _snapshots, masses, means, variances = solve

    output_path = plot_comparison(
        x_positions, y_positions, t_track, x_track, y_track, solve, output
    )

    print_diagnostics(diagnostics(masses, means, variances))
    print(f"\nSaved plot to: {output_path}")
    return output_path


def main() -> None:
    """Console-script entry point."""
    run()


if __name__ == "__main__":
    main()
