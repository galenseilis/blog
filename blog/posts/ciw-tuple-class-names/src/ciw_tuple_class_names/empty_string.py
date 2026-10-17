"""Mixed-type tuples are fixed by padding with a matching type.

The workaround from the post is to keep every tuple the same length and give
each position a consistent type. Replacing the string ``"Child"`` with the
empty string ``""`` keeps the first element a ``str``, so ``("Baby", 0)`` and
``("", 1)`` order without error.
"""

from __future__ import annotations

import ciw


def build_network() -> ciw.network.Network:
    """Return the network with empty-string-padded tuple class names."""
    return ciw.create_network(
        arrival_distributions={
            ("Baby", 0): [
                ciw.dists.Exponential(rate=1.0),
                None,
                None,
            ],
            ("", 1): [
                ciw.dists.Exponential(rate=2.0),
                None,
                None,
            ],
        },
        service_distributions={
            ("Baby", 0): [
                ciw.dists.Exponential(rate=4.0),
                ciw.dists.Exponential(rate=1.0),
                ciw.dists.Deterministic(value=0.0),
            ],
            ("", 1): [
                ciw.dists.Exponential(rate=6.0),
                ciw.dists.Deterministic(value=0.0),
                ciw.dists.Exponential(rate=1.0),
            ],
        },
        routing={
            ("Baby", 0): [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
            ("", 1): [
                [0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        },
        number_of_servers=[1, 2, 3],
    )


def run_simulation(max_time: float = 9) -> ciw.Simulation:
    """Create the network and simulate it until ``max_time``."""
    network = build_network()
    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(max_time)
    return simulation


def main() -> None:
    """Run the padded simulation (no printed output in the post)."""
    run_simulation()


if __name__ == "__main__":
    main()
