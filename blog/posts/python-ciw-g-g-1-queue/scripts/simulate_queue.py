"""Simulate a G/G/1 queue with Ciw and collect the customer records."""

import ciw

ciw.seed(2018)

arrival_dist = ciw.dists.HyperExponential(rates=[9, 5, 6, 1], probs=[0.2, 0.1, 0.6, 0.1])
service_dist = ciw.dists.Gamma(shape=0.6, scale=1.2)
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [arrival_dist],
    service_distributions = [service_dist],
    number_of_servers = [1]
    )

simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
