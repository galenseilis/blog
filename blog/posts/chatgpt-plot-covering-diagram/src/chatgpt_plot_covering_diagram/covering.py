"""Plot a directed graph according to the rules of a covering diagram.

This is the code ChatGPT produced for the blog post
*Asking ChatGPT to Code a Plotting Function for Covering Diagrams*, kept
faithful to the original answer. The post goes on to show that the
function is *not* a correct covering-diagram plotter for general partial
orders; the package records the attempt so the critique can be checked
against a single source of truth.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.axes import Axes


def covering_diagram(dg: nx.DiGraph, ax: Axes | None = None) -> Axes:
    """Plot the directed graph according to the rules of a covering diagram.

    Parameters
    ----------
    dg : networkx.DiGraph
        The partial order to draw. Nodes are laid out one per level along
        the result of ``networkx.topological_sort``, and the edges that the
        function believes to be covering relations are drawn in red.
    ax : matplotlib.axes.Axes, optional
        The axes to draw on. A new figure is created when this is omitted,
        which makes the function usable both standalone and as one panel of
        a larger figure.

    Returns
    -------
    matplotlib.axes.Axes
        The axes the graph was drawn on, so callers can save or annotate it.
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
    if ax is None:
        _fig, ax = plt.subplots(figsize=(8, 8))
    nx.draw_networkx_nodes(dg, pos, node_color="white", node_size=1000, ax=ax)
    nx.draw_networkx_labels(dg, pos, ax=ax)
    nx.draw_networkx_edges(
        dg, pos, edgelist=dg.edges(), arrows=True, alpha=0.5, ax=ax
    )
    nx.draw_networkx_edges(
        dg, pos, edgelist=edges, edge_color="r", arrows=True, alpha=0.5, ax=ax
    )
    ax.axis("off")
    return ax
