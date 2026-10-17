"""Simulate an M/G/k queue using Ciw."""

from __future__ import annotations

import ciw


def run_simulation(
    seed: int = 2018,
    arrival_time: float = 1.0,
    service_shape: float = 0.6,
    service_scale: float = 1.2,
    num_servers: int = 2,
    horizon: float = 365.0,
) -> list:
    """Run a simulation of an M/G/k queue and return all records.

    Parameters
    ----------
    seed
        Random seed for reproducibility.
    arrival_time
        Mean interarrival time for the exponential distribution.
    service_shape
        Shape parameter for the gamma service distribution.
    service_scale
        Scale parameter for the gamma service distribution.
    num_servers
        Number of servers.
    horizon
        Maximum simulation time.

    Returns
    -------
    list
        All simulation records.
    """
    ciw.seed(seed)

    network = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(arrival_time)],
        service_distributions=[
            ciw.dists.Gamma(shape=service_shape, scale=service_scale)
        ],
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
