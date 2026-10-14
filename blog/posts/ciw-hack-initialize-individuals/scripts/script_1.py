import ciw

import pandas as pd

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[3]
)


Q = ciw.Simulation(N)

# Directly setting individuals to Node 1 (a queue)
Q.nodes[1].individuals = [[ciw.Individual(-i) for i in range(100)]]

Q.simulate_until_max_time(1000)

recs = pd.DataFrame(Q.get_all_records())
