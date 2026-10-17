"""Kelly network simulation using Ciw."""
from __future__ import annotations

import ciw


def run_simulation(
    horizon: float = 9,
    seed: int = 2018,
) -> tuple[ciw.Simulation, list[ciw.Record]]:
    """Run Kelly network simulation and return simulation object and records."""
    ciw.seed(seed)

    network = ciw.create_network(
        arrival_distributions={
            "Baby": [
                ciw.dists.Exponential(rate=1.0),
                None,
                None,
            ],
            "Child": [
                ciw.dists.Exponential(rate=2.0),
                None,
                None,
            ],
        },
        service_distributions={
            "Baby": [
                ciw.dists.Exponential(rate=4.0),
                ciw.dists.Exponential(rate=1.0),
                ciw.dists.Deterministic(value=0.0),
            ],
            "Child": [
                ciw.dists.Exponential(rate=6.0),
                ciw.dists.Deterministic(value=0.0),
                ciw.dists.Exponential(rate=1.0),
            ],
        },
        routing={
            "Baby": [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
            "Child": [
                [0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        },
        number_of_servers=[1, 2, 3],
    )

    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(horizon)
    records = simulation.get_all_records()
    return simulation, records


def main() -> None:
    """Main entry point for the simulation."""
    _, records = run_simulation()
    for record in records:
        print(record)


if __name__ == "__main__":
    main()
