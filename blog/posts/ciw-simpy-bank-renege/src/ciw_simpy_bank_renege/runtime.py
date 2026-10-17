"""Sample many Bank Renege run times and fit a Gamma distribution.

The post estimates the distribution of the time for all five customers to
sojourn by simulating many times and fitting a Gamma distribution to the
results. This module reproduces that experiment: sample, fit, histogram, and
overlay the fitted density.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

from ciw_simpy_bank_renege.network import build_network, max_customers, seed

n_simulations = 1_000_000

output_path = "figures/bank-renege-run-times.png"


def run_time(network) -> float:
    """Return the sojourn time for all five customers in one simulation.

    Parameters
    ----------
    network:
        A network from
        :func:`ciw_simpy_bank_renege.network.build_network`. Ciw copies the
        network for each simulation, so it can be reused.
    """
    import ciw

    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_customers(max_customers, method="Finish")
    return max(record.exit_date for record in simulation.get_all_records())


def sample_run_times(
    n: int = n_simulations, random_seed: int = seed
) -> np.ndarray:
    """Return ``n`` simulated sojourn times.

    Parameters
    ----------
    n:
        The number of simulations to run. Defaults to one million, as in the
        post.
    random_seed:
        Seed for Ciw's random number generator.

    Returns
    -------
    numpy.ndarray
        The simulated sojourn times.
    """
    import ciw

    ciw.seed(random_seed)
    network = build_network()
    return np.array([run_time(network) for _ in range(n)])


def fit_gamma(x: np.ndarray):
    """Fit a Gamma distribution to ``x`` and return its parameters."""
    return gamma.fit(x)


def plot_run_times(
    x: np.ndarray,
    output: str = output_path,
    bins: int = 200,
) -> tuple:
    """Histogram the run times and overlay a fitted Gamma density.

    Parameters
    ----------
    x:
        The simulated sojourn times.
    output:
        Where to save the figure.
    bins:
        Number of histogram bins.

    Returns
    -------
    tuple
        The fitted Gamma parameters ``(shape, loc, scale)``.
    """
    plt.style.use("dark_background")
    params = fit_gamma(x)
    q = np.linspace(x.min(), x.max(), num=100)
    p = gamma.pdf(q, *params)

    plt.hist(x, density=True, bins=bins)
    plt.plot(
        q,
        p,
        label=f"Gamma(shape={np.round(params[0], 2)},scale={np.round(params[2], 2)})",
    )
    plt.xlabel("Simulation Time")
    plt.ylabel("Density")
    plt.legend()
    plt.savefig(output, dpi=300, transparent=True)
    plt.close()
    return params


def main() -> None:
    """Simulate one million run times and save the fitted-density plot."""
    x = sample_run_times()
    plot_run_times(x)


if __name__ == "__main__":
    main()
