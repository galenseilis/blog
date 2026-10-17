"""Assemble the Ciw network and run the Snakes and Ladders simulation.

This is the complete example from the post: it puts together the routing
matrix, the arrival, service, and batching distributions, and the number of
servers into a single :func:`ciw.create_network` call, simulates until a player
reaches the final square, and reports that player as the winner.
"""

from __future__ import annotations

import ciw
import pandas as pd

from ciw_snakes_ladders.arrivals import build_arrival_distributions
from ciw_snakes_ladders.batching import build_batching_distributions
from ciw_snakes_ladders.board import build_routing_matrix, n_squares
from ciw_snakes_ladders.servers import build_number_of_servers
from ciw_snakes_ladders.services import build_service_distributions

seed = 2018


def build_network() -> ciw.network.Network:
    """Create the Ciw network for the board.

    Returns
    -------
    ciw.network.Network
        The fully specified network, ready to be handed to
        :class:`ciw.Simulation`.
    """
    return ciw.create_network(
        arrival_distributions=build_arrival_distributions(),
        service_distributions=build_service_distributions(),
        routing=build_routing_matrix(),
        batching_distributions=build_batching_distributions(),
        number_of_servers=build_number_of_servers(),
    )


def run_simulation(random_seed: int = seed) -> ciw.Simulation:
    """Simulate until one player reaches the end of the board.

    Parameters
    ----------
    random_seed:
        Seed for Ciw's random number generator, for repeatability.

    Returns
    -------
    ciw.Simulation
        The simulation, after running until a single customer has finished.
    """
    ciw.seed(random_seed)
    network = build_network()
    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_customers(1, method="Finish")
    return simulation


def winner(simulation: ciw.Simulation) -> int:
    """Return the id number of the player who reached the final square.

    Parameters
    ----------
    simulation:
        A simulation that has been run to completion.

    Returns
    -------
    int
        The ``id_number`` of the first player routed into the final square.
    """
    records = pd.DataFrame(simulation.get_all_records())
    return records[records.destination == n_squares].id_number.to_numpy()[0]


def main() -> None:
    """Run the simulation and print the winner."""
    simulation = run_simulation()
    print(f"Player {winner(simulation)} is the winner!")


if __name__ == "__main__":
    main()
