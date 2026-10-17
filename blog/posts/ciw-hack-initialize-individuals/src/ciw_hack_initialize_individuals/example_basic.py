"""Basic example."""

from __future__ import annotations

import ciw
import pandas as pd


def main() -> None:
    network = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
        service_distributions=[ciw.dists.Exponential(rate=0.1)],
        number_of_servers=[3],
    )
    sim = ciw.Simulation(network)
    sim.nodes[1].individuals = [[ciw.Individual(-i) for i in range(100)]]
    sim.simulate_until_max_time(1000)
    recs = pd.DataFrame(sim.get_all_records())
    print(recs.head())
