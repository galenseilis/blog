"""Example usage from the blog post."""

from __future__ import annotations

import ciw
import numpy as np
import pandas as pd

from ciw_dirichlet_sampling_router_matrix import RandomDirichletList


def run_example() -> pd.DataFrame:
    """Run the example with resampling routing matrix."""
    np.random.seed(seed=2018)

    sm = [
        RandomDirichletList([1, 2, 3]),
        RandomDirichletList([3, 4, 5]),
        RandomDirichletList([6, 7, 8]),
    ]

    network = ciw.create_network(
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
        routing=sm,
        number_of_servers=[1, 2, 2],
    )

    sim = ciw.Simulation(network)
    sim.simulate_until_max_time(10)
    df = pd.DataFrame(sim.get_all_records())
    return df


def main() -> None:
    df = run_example()
    print(df.to_markdown())


if __name__ == "__main__":
    main()
