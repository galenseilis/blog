import ciw

ciw.seed(2018)

ARRIVAL_TIME = 1
SERVICE_TIME = 1 / 2
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(ARRIVAL_TIME)],
    service_distributions = [ciw.dists.Deterministic(SERVICE_TIME)],
    number_of_servers = [1]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
