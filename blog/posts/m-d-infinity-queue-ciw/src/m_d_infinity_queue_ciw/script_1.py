import ciw

ciw.seed(2018)

ARRIVAL_TIME = 1
SERVICE_TIME = 1 / 2
NUM_SERVERS = float('inf')
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(ARRIVAL_TIME)],
    service_distributions = [ciw.dists.Exponential(SERVICE_TIME)],
    number_of_servers = [NUM_SERVERS]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
