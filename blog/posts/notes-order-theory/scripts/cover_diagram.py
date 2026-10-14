"""Draw a cover diagram for an example strict partial order."""

import os
import warnings

import matplotlib.pyplot as plt
import networkx as nx


g = nx.Graph()

g.add_edge('a', 'c')
g.add_edge('a', 'e')
g.add_edge('b', 'c')
g.add_edge('b', 'd')
g.add_edge('d', 'e')

pos = {'a': (0, 1),
       'b': (1, 0),
       'c': (0, 3),
       'd': (2, 2),
       'e': (1, 4)}

with warnings.catch_warnings():
    warnings.filterwarnings('ignore')
    nx.draw(g, pos=pos, labels={i: i for i in g.nodes()}, node_color=(0.5,) * 3)

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "cover_diagram.png"), dpi=300, bbox_inches="tight")
plt.close()
