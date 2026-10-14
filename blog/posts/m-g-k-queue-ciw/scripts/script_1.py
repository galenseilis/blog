import ciw

ciw.seed(2018)

ARRIVAL_TIME = 1
SERVICE_SHAPE = 6 / 10
SERVICE_SCALE = 12 / 10
NUM_SERVERS = 2
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(ARRIVAL_TIME)],
    service_distributions = [ciw.dists.Gamma(shape=SERVICE_SHAPE, scale=SERVICE_SCALE)],
    number_of_servers = [NUM_SERVERS]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
