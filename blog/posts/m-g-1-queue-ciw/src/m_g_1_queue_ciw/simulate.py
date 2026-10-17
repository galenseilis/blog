"""M/G/1 queue simulation logic."""
import ciw


def run_simulation(
    arrival_time=1,
    service_shape=6 / 10,
    service_scale=12 / 10,
    horizon=365,
    seed=2018,
):
    """Run M/G/1 queue simulation and return simulation object and records."""
    ciw.seed(seed)

    network = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(arrival_time)],
        service_distributions=[ciw.dists.Gamma(shape=service_shape, scale=service_scale)],
        number_of_servers=[1],
    )

    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(horizon)
    records = simulation.get_all_records()
    return simulation, records


def main():
    """Main entry point for the simulation."""
    _, records = run_simulation()
    for record in records[:10]:
        print(record)


if __name__ == "__main__":
    main()
