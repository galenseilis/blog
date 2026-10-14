from itertools import product
import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import rankdata
import semopy

# Utils

def decycle(d):
    '''
    Pseudorandomly remove cycles from a directed graph.

    Changes the graph inplace.

    PARAMETERS
    ----------
    d : networkx.DiGraph
        Directed graph.

    RETURNS
    -------
    None
    '''
    while True:
        if nx.is_directed_acyclic_graph(d):
            break
        first_cycle = nx.cycles.find_cycle(d)
        target_edge = random.sample(first_cycle, 1)[0]
        d.remove_edge(*target_edge)

rank = lambda x: rankdata(x, method='dense', axis=0)

# Config
n = 100
m = 1000
possible_edges = list(product(range(n), repeat=2))
np.random.seed(2018)

# Generate a DAG
d = nx.DiGraph()
edges = random.sample(possible_edges, n)
d.add_edges_from(edges)
decycle(d)

# Create Lavaan-style string following DAG
model_str = ''
for node in nx.topological_sort(d):
    node_str = f''
    for i, edge in enumerate(d.out_edges(node)):
        if i == 0:
            node_str += f'x{edge[1]}'
        else:
            node_str += f'+x{edge[1]}'
    if node_str:
        model_str += f'x{node} ~ {node_str}\n'

print(model_str)
model = semopy.Model(model_str)


# Generate data that follows DAG
data = np.random.normal(size=m*n).reshape(m,n)
betas = {edge:np.random.normal(scale=10) for edge in d.edges()}
for node in nx.topological_sort(d):
    for edge in d.out_edges(node):
        data[:,node] += betas[edge] * data[:,edge[1]]

df = pd.DataFrame(data, columns=[f'x{i}' for i in range(n)])
df_rank = pd.DataFrame(rank(data), columns=[f'x{i}' for i in range(n)])

# Train model on data
print('Training model on data')
linear_results = model.fit(df)
linear_inspection = model.inspect()
linear_inspection.to_markdown('sem_linear_inspection.md', index=False)
semopy.semplot(model, 'sem_model.png', plot_covs=True, show=True)

# Train model on ranks of data
print('Training model on rank data')
rank_results = model.fit(df_rank)
rank_inspection = model.inspect()
rank_inspection.to_markdown('sem_rank_inspection.md', index=False)
semopy.semplot(model, 'sem_model_ranks.png', plot_covs=True, show=True)
