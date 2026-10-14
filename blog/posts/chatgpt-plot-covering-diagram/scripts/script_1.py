import networkx as nx
import matplotlib.pyplot as plt
def covering_diagram(dg):
    """
    Plot the directed graph according to the rules of a covering diagram.
    """
    levels = list(nx.topological_sort(dg))
    pos = {}
    for i, level in enumerate(levels):
        for j, node in enumerate(level):
            pos[node] = (j, -i)
    # Create a list of edges to add for the covering relations
    edges = []
    for i in range(len(levels) - 1):
        for a in levels[i]:
            for b in levels[i + 1]:
                if set(dg.predecessors(b)).issubset(set(dg.predecessors(a))):
                    edges.append((a, b))
    # Create the plot
    plt.figure(figsize=(8, 8))
    nx.draw_networkx_nodes(dg, pos, node_color='white', node_size=1000)
    nx.draw_networkx_labels(dg, pos)
    nx.draw_networkx_edges(dg, pos, edgelist=dg.edges(), arrows=True, alpha=0.5)
    nx.draw_networkx_edges(dg, pos, edgelist=edges, edge_color='r', arrows=True, alpha=0.5)
    plt.axis('off')
    plt.show()
