"""Plot the word adjacency graph for *The Little Irish Girl*."""

import os

import matplotlib.pyplot as plt
import networkx as nx

from .lyrics import lyrics


def create_graph(strings):
    G = nx.DiGraph()
    for s in strings:
        G.add_node(s)
    for i in range(len(strings) - 1):
        G.add_edge(strings[i], strings[i + 1])
    return G


def plot_graph(G):
    try:
        pos = nx.nx_agraph.graphviz_layout(G)
    except ImportError:
        pos = nx.spring_layout(G, seed=2018)
    node_sizes = [len(node) * 100 for node in G.nodes()]
    plt.figure(figsize=(8, 30))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        font_size=10,
        node_size=node_sizes,
        font_weight="bold",
        arrows=True,
    )
    plt.title("Word Adjacency in The Little Irish Girl", fontsize=14)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    post_dir = os.path.abspath(os.path.join(here, os.pardir, os.pardir))
    figures_dir = os.path.join(post_dir, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    graph = create_graph(lyrics)
    plot_graph(graph)
    plt.savefig(os.path.join(figures_dir, "word-adjacency.png"), dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
