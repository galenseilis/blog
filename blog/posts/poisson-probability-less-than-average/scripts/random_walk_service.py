"""Simulate a queue at unity utilization and plot the resulting random-walk waiting times."""

import os

import ciw
import pandas as pd


def main():
    ciw.seed(2018)

    model_spec = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=3)],
        service_distributions=[ciw.dists.Exponential(rate=1)],
        number_of_servers=[3],
    )

    simulation = ciw.Simulation(model_spec)
    simulation.simulate_until_max_time(2018)

    results = pd.DataFrame(simulation.get_all_records())
    ax = results.plot(x="service_start_date", y="waiting_time")

    here = os.path.dirname(os.path.abspath(__file__))
    figures_dir = os.path.join(here, os.pardir, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    ax.get_figure().savefig(
        os.path.join(figures_dir, "random_walk_service.png"),
        dpi=300,
        bbox_inches="tight",
    )


if __name__ == "__main__":
    main()
