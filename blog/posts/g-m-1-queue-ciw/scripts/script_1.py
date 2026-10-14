import ciw

ciw.seed(2018)

ARRIVAL_SHAPE = 6 / 10
ARRIVAL_SCALE = 12 / 10
SERVICE_TIME = 1
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Gamma(shape=ARRIVAL_SHAPE, scale=ARRIVAL_SCALE)],
    service_distributions = [ciw.dists.Exponential(SERVICE_TIME)],
    number_of_servers = [1]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
