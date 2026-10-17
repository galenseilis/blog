"""The example partial order from the notes and its digraph representation.

The ground set is ``X = {a, b, c, d, e}`` and the relation is

    {(a, a), (a, c), (a, e), (b, b), (b, c), (b, d), (b, e),
     (c, c), (d, d), (d, e), (e, e)}.

Because the relation is reflexive it includes the five self-pairs, which the
digraph draws as self-loops.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

EXAMPLE_ORDER: list[str] = [
    "aa",
    "ac",
    "ae",
    "bb",
    "bc",
    "bd",
    "be",
    "cc",
    "dd",
    "de",
    "ee",
]
"""The example relation, with each ordered pair written as a two-character string."""


def build_digraph(order: list[str] | None = None) -> nx.DiGraph:
    """Build the directed-graph representation of a partial order.

    ``order`` is a list of two-character strings, each the head and tail of an
    ordered pair. It defaults to :data:`EXAMPLE_ORDER`.
    """
    graph = nx.DiGraph()
    for pair in order if order is not None else EXAMPLE_ORDER:
        graph.add_edge(pair[0], pair[1])
    return graph


def plot_example_partial_order(
    output: str | Path = "figures/example_partial_order.png",
) -> Path:
    """Draw the digraph of the example partial order and save it.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    graph = build_digraph()
    pos = nx.spring_layout(graph, seed=2018)
    fig, ax = plt.subplots()
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        nx.draw(
            graph,
            pos=pos,
            labels={node: node for node in graph.nodes()},
            node_color=(0.5,) * 3,
            with_labels=True,
            arrows=True,
            ax=ax,
        )

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point: draw the example digraph."""
    plot_example_partial_order()


if __name__ == "__main__":
    main()
