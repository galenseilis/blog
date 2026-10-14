from script_2 import np
from script_2 import RandomDirichletList
import ciw
import numpy
import pandas as pd

np.random.seed(seed=2018)

# Assume RandomDirichletList is in namespace

sm = [
    RandomDirichletList([1, 2, 3]),
    RandomDirichletList([3, 4, 5]),
    RandomDirichletList([6, 7, 8]),
]

N = ciw.create_network(
    arrival_distributions=[
        ciw.dists.Exponential(rate=0.3),
        ciw.dists.Exponential(rate=0.2),
        None,
    ],
    service_distributions=[
        ciw.dists.Exponential(rate=1.0),
        ciw.dists.Exponential(rate=0.4),
        ciw.dists.Exponential(rate=0.5),
    ],
    routing=sm,
    number_of_servers=[1, 2, 2],
)

sim = ciw.Simulation(N)
sim.simulate_until_max_time(10)

pd.DataFrame(
    sim.get_all_records()
    ).to_markdown('out.md')
