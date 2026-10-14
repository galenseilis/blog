from itertools import product
import random
from time import ctime

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import rankdata
import semopy

# Utils


def decycle(d):
    """
    Pseudorandomly remove cycles from a directed graph.

    Changes the graph inplace.

    PARAMETERS
    ----------
    d : networkx.DiGraph
        Directed graph.

    RETURNS
    -------
    None
    """
    while True:
        if nx.is_directed_acyclic_graph(d):
            break
        first_cycle = nx.cycles.find_cycle(d)
        target_edge = random.sample(first_cycle, 1)[0]
        d.remove_edge(*target_edge)


rank = lambda x: rankdata(x, method="dense", axis=0)

# Config
k = 100
n = 100
m = 1000
possible_edges = list(product(range(n), repeat=2))
np.random.seed(2018)
linear_scores = []
rank_scores = []

for _ in range(k):
    # Generate a DAG
    d = nx.DiGraph()
    edges = random.sample(possible_edges, n)
    d.add_edges_from(edges)
    decycle(d)

    # Create Lavaan-style string following DAG
    model_str = ""
    for node in nx.topological_sort(d):
        node_str = f""
        for i, edge in enumerate(d.out_edges(node)):
            if i == 0:
                node_str += f"x{edge[1]}"
            else:
                node_str += f"+x{edge[1]}"
        if node_str:
            model_str += f"x{node} ~ {node_str}\n"

    ##    print(model_str)
    model = semopy.Model(model_str)

    # Generate data that follows DAG
    data = np.random.normal(size=m * n).reshape(m, n)
    betas = {edge: np.random.normal(scale=10) for edge in d.edges()}
    str_betas = {
        frozenset((f"x{k1}", f"x{k2}")): val for (k1, k2), val in betas.items()
    }
    for node in nx.topological_sort(d):
        for edge in d.out_edges(node):
            data[:, node] += betas[edge] * data[:, edge[1]]

    df = pd.DataFrame(data, columns=[f"x{i}" for i in range(n)])
    df_rank = pd.DataFrame(rank(data), columns=[f"x{i}" for i in range(n)])

    # Train model on data
    linear_results = model.fit(df)
    linear_inspection = model.inspect()

    linear_inspection = linear_inspection[linear_inspection["op"] == "~"]
    linear_inspection["true_beta"] = linear_inspection[
        linear_inspection["op"] == "~"
    ].apply(lambda row: str_betas[frozenset([row.rval, row.lval])], axis=1)
    linear_score = (
        linear_inspection["Estimate"].apply(np.sign)
        == linear_inspection["true_beta"].apply(np.sign)
    ).mean()
    linear_scores.append(linear_score)

    # Train model on ranks of data
    rank_results = model.fit(df_rank)
    rank_inspection = model.inspect()

    rank_inspection = rank_inspection[rank_inspection["op"] == "~"]
    rank_inspection["true_beta"] = rank_inspection[rank_inspection["op"] == "~"].apply(
        lambda row: str_betas[frozenset([row.rval, row.lval])], axis=1
    )
    rank_score = (
        rank_inspection["Estimate"].apply(np.sign)
        == rank_inspection["true_beta"].apply(np.sign)
    ).mean()
    rank_scores.append(rank_score)

    print(_, ctime(), linear_score, rank_score)

# Some plots
plt.scatter(
    rank_inspection["true_beta"],
    rank_inspection["Estimate"].apply(np.sign)
    == rank_inspection["true_beta"].apply(np.sign),
)
plt.xlabel(r"$\beta$")
plt.ylabel(
    r"$\mathbb{I} \left[ \operatorname{sign}(\hat \beta) = \operatorname{sign}(\beta) \right]$"
)
plt.savefig("rank_sem_equal_signum_vs_param.png", dpi=300, transparent=True)
plt.close()

plt.scatter(rank_scores, linear_scores)
plt.xlabel("Prob. of Signum Match With Rank SEM")
plt.ylabel("Prob. of Signum Match With Linear SEM")
plt.savefig("prob_signum_match_sem.png", transparent=True)
plt.close()
