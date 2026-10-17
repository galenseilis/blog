"""The cover diagram of the example strict partial order.

The strict partial order is

    {(a, c), (a, e), (b, c), (b, d), (b, e), (d, e)}.

Its cover relation drops ``(b, e)`` because ``b < d < e``, leaving the edges
``a-c``, ``a-e``, ``b-c``, ``b-d`` and ``d-e``. The nodes are laid out so that
each cover edge goes upward, which is what makes the drawing a cover diagram.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

COVER_POSITIONS: dict[str, tuple[float, float]] = {
    "a": (0.0, 1.0),
    "b": (1.0, 0.0),
    "c": (0.0, 3.0),
    "d": (2.0, 2.0),
    "e": (1.0, 4.0),
}
"""Fixed node positions: drawing an edge moves strictly upwards."""

COVER_EDGES: list[tuple[str, str]] = [
    ("a", "c"),
    ("a", "e"),
    ("b", "c"),
    ("b", "d"),
    ("d", "e"),
]
"""The cover pairs of the example strict partial order."""


def build_cover_graph(edges: list[tuple[str, str]] | None = None) -> nx.Graph:
    """Build the (undirected) cover graph of the example partial order."""
    graph = nx.Graph()
    graph.add_edges_from(edges if edges is not None else COVER_EDGES)
    return graph


def plot_cover_diagram(
    output: str | Path = "figures/cover_diagram.png",
) -> Path:
    """Draw the cover diagram of the example partial order and save it.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    graph = build_cover_graph()
    fig, ax = plt.subplots()
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        nx.draw(
            graph,
            pos=COVER_POSITIONS,
            labels={node: node for node in graph.nodes()},
            node_color=(0.5,) * 3,
            with_labels=True,
            ax=ax,
        )

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point: draw the cover diagram."""
    plot_cover_diagram()


if __name__ == "__main__":
    main()
