"""Run the cafe example from the Ciw documentation.

This is the model being visualised: a three-node cafe with separate cold-food
and hot-food preparation stations feeding a till. Arrivals come in at two
rates, and after being served at the till everyone exits.
"""

from __future__ import annotations

import ciw
import pandas as pd

seed = 2018

max_time = 200


def build_network() -> ciw.network.Network:
    """Return the cafe network from the Ciw documentation.

    Returns
    -------
    ciw.network.Network
        A three-node network: ``ColdFood`` (1), ``HotFood`` (2), and ``Till``
        (3).
    """
    return ciw.create_network(
        arrival_distributions=[
            ciw.dists.Exponential(rate=0.3),
            ciw.dists.Exponential(rate=0.2),
            None,
        ],
        service_distributions=[
            ciw.dists.Exponential(rate=1.0),
            ciw.dists.Exponential(rate=0.4),
            ciw.dists.Exponential(rate=0.5),
        ],
        routing=[[0.0, 0.3, 0.7], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]],
        number_of_servers=[1, 2, 2],
    )


def run_simulation(
    simulation_time: float = max_time, random_seed: int = seed
) -> ciw.Simulation:
    """Seed Ciw, build the network, and simulate until ``simulation_time``.

    Parameters
    ----------
    simulation_time:
        The time to simulate until.
    random_seed:
        Seed for Ciw's random number generator, for repeatability.

    Returns
    -------
    ciw.Simulation
        The simulation after running.
    """
    ciw.seed(random_seed)
    network = build_network()
    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(simulation_time)
    return simulation


def get_records(simulation: ciw.Simulation) -> pd.DataFrame:
    """Return the simulation's records as a DataFrame."""
    return pd.DataFrame(simulation.get_all_records())
