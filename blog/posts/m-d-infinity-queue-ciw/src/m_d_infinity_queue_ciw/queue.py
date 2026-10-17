"""Simulate an M/M/∞ queue using Ciw."""

from __future__ import annotations

import ciw


def run_simulation(
    seed: int = 2018,
    arrival_time: float = 1.0,
    service_time: float = 0.5,
    horizon: float = 365.0,
) -> list:
    """Run a simulation of an M/M/∞ queue and return all records.

    Parameters
    ----------
    seed
        Random seed for reproducibility.
    arrival_time
        Mean interarrival time for the exponential distribution.
    service_time
        Mean service time for the exponential distribution.
    horizon
        Maximum simulation time.

    Returns
    -------
    list
        All simulation records.
    """
    ciw.seed(seed)

    num_servers = float("inf")
    network = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(arrival_time)],
        service_distributions=[ciw.dists.Exponential(service_time)],
        number_of_servers=[num_servers],
    )

    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(horizon)
    return simulation.get_all_records()


def main() -> None:
    """Execute the simulation and print results."""
    records = run_simulation()
    print(records)


if __name__ == "__main__":
    main()
