from script_1 import x1
from script_1 import x2
from script_1 import x3
from script_1 import x5
from script_1 import x4
import networkx as nx

g = nx.DiGraph()

g.add_edge(x1, x2)
g.add_edge(x1, x3)
g.add_edge(x2, x5)
g.add_edge(x3, x4)
g.add_edge(x4, x5)
