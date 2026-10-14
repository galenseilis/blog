import ciw

import pandas as pd


def print_has_simulation_LIFO(individuals, now=None):

    if individuals[-1].id_number <= 0:
        print(individuals[-1].id_number, individuals[-1].simulation)

    return individuals[-1]

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    service_disciplines=[print_has_simulation_LIFO],
    number_of_servers=[3]
)


Q = ciw.Simulation(N)

# Ensure the instances have the simulation instance
init_individuals = []
for i in range(10):
    initial_ind = ciw.Individual(-i, simulation=Q)
    init_individuals.append(initial_ind)
    
Q.nodes[1].individuals = [init_individuals]

Q.simulate_until_max_time(1000)
