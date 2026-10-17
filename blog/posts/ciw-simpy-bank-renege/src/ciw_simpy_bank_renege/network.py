"""The Bank Renege network and its simulation.

The model is an M/M/1 queue with two custom features:

* only five customers ever arrive, enforced by
  :class:`~ciw_simpy_bank_renege.max_arrival.MaxArrivalDist`;
* waiting customers renege after a uniformly distributed patience time.

The simulation runs until five customers have *finished* (been served and left,
whether by service or by reneging), so the time at the end of the simulation is
the sojourn time for all five customers.
"""

from __future__ import annotations

import ciw

from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist

arrival_rate = 1 / 10

service_rate = 1 / 12

max_customers = 5

reneging_time = (1, 3)

seed = 2018


def build_network() -> ciw.network.Network:
    """Return the Bank Renege network.

    Returns
    -------
    ciw.network.Network
        A single-server network with bounded arrivals and reneging.
    """
    return ciw.create_network(
        arrival_distributions=[
            MaxArrivalDist(ciw.dists.Exponential(arrival_rate), max_customers)
        ],
        service_distributions=[ciw.dists.Exponential(service_rate)],
        number_of_servers=[1],
        reneging_time_distributions=[ciw.dists.Uniform(*reneging_time)],
    )


def run_simulation(random_seed: int = seed) -> ciw.Simulation:
    """Simulate until all five customers have left the system.

    Parameters
    ----------
    random_seed:
        Seed for Ciw's random number generator, for repeatability.

    Returns
    -------
    ciw.Simulation
        The simulation after running to the finish of five customers.
    """
    ciw.seed(random_seed)
    network = build_network()
    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_customers(max_customers, method="Finish")
    return simulation
