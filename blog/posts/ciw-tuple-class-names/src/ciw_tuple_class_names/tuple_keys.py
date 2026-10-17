"""Two customer classes named by consistently-shaped tuples.

Both class names are ``(str, int)`` pairs, so Python's lexicographic tuple
ordering compares like with like, and Ciw accepts them. This is the first
demonstration in the post: tuples work as class names so long as every tuple
can be ordered against the others.
"""

from __future__ import annotations

import ciw


def build_network() -> ciw.network.Network:
    """Return a three-node network with two tuple-named customer classes."""
    return ciw.create_network(
        arrival_distributions={
            ("Baby", 0): [
                ciw.dists.Exponential(rate=1.0),
                None,
                None,
            ],
            ("Child", 1): [
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
            ("Child", 1): [
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
            ("Child", 1): [
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
    """Run the simulation (no printed output in the post)."""
    run_simulation()


if __name__ == "__main__":
    main()
