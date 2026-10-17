"""The full worked example partial order from the blog post."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from chatgpt_plot_covering_diagram.covering import covering_diagram


def full_example(
    output: str | Path = "figures/chatgpt_cover_relation_plotter_output.png",
) -> Path:
    """Draw the full worked example from the post and save it.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    dg = nx.DiGraph()
    dg.add_nodes_from(["a", "b", "c", "d", "e", "f"])
    dg.add_edges_from(
        [
            ("a", "b"),
            ("a", "c"),
            ("a", "d"),
            ("b", "e"),
            ("c", "e"),
            ("d", "e"),
            ("e", "f"),
        ]
    )
    ax = covering_diagram(dg)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(output_path, dpi=300, transparent=True)
    plt.close(ax.figure)
    return output_path


def main() -> None:
    """Console-script entry point: render the full worked example."""
    full_example()


if __name__ == "__main__":
    main()
