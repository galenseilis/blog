"""Visualize a tangent vector in terms of the differential axes.

The figure draws the vector ``<c, d>`` at the point ``(1, 1)`` against the
differential axes ``dx`` and ``dy``, with the ambient coordinates ``a`` and
``b`` marked on the axes.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def plot_tangent_space_axes(
    output: str | Path = "figures/tangent_space_axes.png",
) -> Path:
    """Draw a tangent vector against the differential axes and save it.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    fig, ax = plt.subplots()
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([0, 3])
    ax.set_ylim([0, 3])
    ax.annotate("", xy=(2, 2), xytext=(1, 1), arrowprops=dict(color="tab:blue"))
    plt.text(2, 2, r"$\langle c,d \rangle_{(a,b)}$", color="gray")
    ax.annotate("", xy=(1, 2.5), xytext=(1, 0.9), arrowprops=dict(color="m"))
    ax.annotate("", xy=(2.5, 1), xytext=(0.9, 1), arrowprops=dict(color="m"))
    ax.text(2.5, 1, "dx", color="grey")
    ax.text(1, 2.5, "dy", color="grey")
    ax.text(2, 1, "c", color="grey")
    ax.text(1, 2, "d", color="grey")
    ax.text(2, 0, "a", color="grey")
    ax.text(0, 2, "b", color="grey")
    fig.tight_layout()

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point."""
    plot_tangent_space_axes()


if __name__ == "__main__":
    main()
