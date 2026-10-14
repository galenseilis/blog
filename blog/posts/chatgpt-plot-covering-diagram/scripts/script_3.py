from script_1 import covering_diagram
import networkx as nx

# Create a directed graph
dg = nx.DiGraph()
dg.add_edges_from([('a','c'), ('a','e'),('b','c'), ('b','d'), ('b','e'), ('d','e')])

# Plot the graph with a covering diagram
covering_diagram(dg)
