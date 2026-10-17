"""Utilities for initializing individuals."""

from __future__ import annotations

import ciw


def initialize_queue_individuals(
    sim: ciw.Simulation, node_id: int, count: int, with_simulation: bool = True
) -> None:
    """Initialize a queue node with pre-existing individuals."""
    init_individuals = []
    for i in range(count):
        ind = ciw.Individual(-(i + 1))
        if with_simulation:
            ind.simulation = sim
        init_individuals.append(ind)
    sim.nodes[node_id].individuals = [init_individuals]
