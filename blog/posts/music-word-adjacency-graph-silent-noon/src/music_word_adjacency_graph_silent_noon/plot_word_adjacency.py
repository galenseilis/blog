"""Plot the word adjacency graph for Rossetti's *Silent Noon*."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from music_word_adjacency_graph_silent_noon.lyrics import lyrics


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
    plt.title("Word Adjacency in Silent Noon", fontsize=14)


def plot_word_adjacency(output: str | Path = "figures/word-adjacency.png") -> Path:
    """Build the word adjacency graph and save it to ``output``.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    graph = create_graph(lyrics)
    plot_graph(graph)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    return output_path


def main() -> None:
    """Console-script entry point."""
    plot_word_adjacency()


if __name__ == "__main__":
    main()
