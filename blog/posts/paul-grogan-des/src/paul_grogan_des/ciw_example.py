import ciw

# Define the parameters for the arrival and service processes
arrival_rate = 3  # Interarrival rate (lambda)
service_rate = 4  # Service rate (mu)

# Define the parameters for the Ciw network
network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(arrival_rate)],
    service_distributions=[ciw.dists.Exponential(service_rate)],
    number_of_servers=[1],
)

# Create and run the simulation
ciw.seed(2018)
sim = ciw.Simulation(network)
sim.simulate_until_max_time(2018)
