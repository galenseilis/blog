"""The smaller partial order the post uses as a failing test case."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from chatgpt_plot_covering_diagram.covering import covering_diagram


def failing_example(
    output: str | Path = "figures/chatgpt_cover_relation_plotter_output_test.png",
) -> Path:
    """Draw the post's failing test case and save it.

    The post expects a diagram similar to ``example_cover_relation_diagram.png``
    but the function produces something else, which is the evidence for the
    author's conclusion that the code does not work.

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
    dg.add_edges_from(
        [("a", "c"), ("a", "e"), ("b", "c"), ("b", "d"), ("b", "e"), ("d", "e")]
    )
    ax = covering_diagram(dg)

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(output_path, dpi=300, transparent=True)
    plt.close(ax.figure)
    return output_path


if __name__ == "__main__":
    failing_example()
