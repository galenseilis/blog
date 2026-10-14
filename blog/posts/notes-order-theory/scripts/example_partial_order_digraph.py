"""Draw a digraph representation of an example partial order."""

import os
import warnings

import matplotlib.pyplot as plt
import networkx as nx


g = nx.DiGraph()

XxX = 'aa', 'ac', 'ae', 'bb', 'bc', 'bd', 'be', 'cc', 'dd', 'de', 'ee'
for xx in XxX:
    g.add_edge(xx[0], xx[1])

pos = nx.spring_layout(g, seed=2018)

with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    nx.draw(g, pos=pos, labels={i: i for i in g.nodes()}, node_color=(0.5,) * 3,
            with_labels=True, arrows=True)

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "example_partial_order.png"), dpi=300, bbox_inches="tight")
plt.close()
