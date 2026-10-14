from script_1 import covering_diagram
import networkx as nx
# Create a directed graph
dg = nx.DiGraph()
dg.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f'])
dg.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('c', 'e'), ('d', 'e'), ('e', 'f')])
# Plot the graph with a covering diagram
covering_diagram(dg)
