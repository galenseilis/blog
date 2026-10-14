"""Plot the word adjacency graph for *Rolling Down to Rio*."""

import os

import matplotlib.pyplot as plt
import networkx as nx

from lyrics import lyrics


def create_graph(strings):
    # Initialize a directed graph
    G = nx.DiGraph()

    # Add each string as a node
    for s in strings:
        G.add_node(s)

    # Create edges based on adjacency (e.g., consecutive strings in the list)
    for i in range(len(strings) - 1):
        G.add_edge(strings[i], strings[i + 1])

    return G


def plot_graph(G):
    # Generate positions for nodes
    try:
        pos = nx.nx_agraph.graphviz_layout(G)
    except ImportError:
        pos = nx.spring_layout(G, seed=2018)

    node_sizes = [len(node) * 100 for node in G.nodes()]  # Adjust 100 to change the scaling factor

    # Draw the graph
    plt.figure(figsize=(8, 30))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=10, node_size=node_sizes, font_weight="bold", arrows=True)
    plt.title("Word Adjacency in Rolling Down to Rio", fontsize=14)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figures_dir = os.path.join(here, os.pardir, "figures")
    os.makedirs(figures_dir, exist_ok=True)

    graph = create_graph(lyrics)
    plot_graph(graph)
    plt.savefig(os.path.join(figures_dir, "word-adjacency.png"), dpi=300, bbox_inches="tight")
