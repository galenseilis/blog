"""G/M/1 queue simulation logic."""
import ciw


def run_simulation(
    arrival_shape=6 / 10,
    arrival_scale=12 / 10,
    service_time=1,
    horizon=365,
    seed=2018,
):
    """Run G/M/1 queue simulation and return simulation object and records."""
    ciw.seed(seed)

    network = ciw.create_network(
        arrival_distributions=[ciw.dists.Gamma(shape=arrival_shape, scale=arrival_scale)],
        service_distributions=[ciw.dists.Exponential(service_time)],
        number_of_servers=[1],
    )

    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(horizon)
    records = simulation.get_all_records()
    return simulation, records


def main():
    """Main entry point for the simulation."""
    _, records = run_simulation()
    # Output to match what the post might expect; print records summary if needed
    for record in records[:10]:  # Print first few records to show output
        print(record)


if __name__ == "__main__":
    main()
