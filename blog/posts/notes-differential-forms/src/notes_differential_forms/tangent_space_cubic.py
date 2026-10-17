"""Plot the tangent space to a cubic curve at a point.

The curve is ``y = x**3 - 10 * x`` and the point is ``(2, -12)``, whose
tangent line is ``y = 2x - 16``. The figure marks the point ``p``, the
tangent space ``T_pC``, the slope, and the pullbacks onto the coordinate
axes.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_tangent_space_cubic(
    output: str | Path = "figures/tangent_space_cubic.png",
) -> Path:
    """Draw the tangent space to the cubic at ``(2, -12)`` and save it.

    Parameters
    ----------
    output : str or pathlib.Path
        Destination of the rendered PNG. Parent directories are created.

    Returns
    -------
    pathlib.Path
        The path that was written.
    """
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 15])
    # Plot of function
    x = np.linspace(-5, 5, num=100)
    y = x**3 - 10 * x
    ax.plot(x, y, color="y")
    # Unit tangent vector
    ax.plot([2, 3], [-12] * 2, "--", color="tab:blue")
    ax.plot([3, 3], [-11, -12], "--", color="tab:blue")
    # Tangent space
    ax.plot(x, 2 * x - 16, color="m")
    ax.text(3, -12, r"$T_pC$", color="m")
    ax.scatter(2, -12, color="m")
    ax.text(2, -14, r"$p$", color="m")
    ax.annotate(
        r"slope$=f^{\prime}(a)$",
        xy=(4, -8),
        xytext=(4, 0),
        arrowprops=dict(facecolor="black", shrink=0.05),
        color="grey",
    )
    # Pullbacks
    ax.plot([2] * 2, [-30, -12], "--", color="m", alpha=0.5)
    ax.text(2, -30, r"$a$", color="m")
    ax.plot([x.min(), 2], [-12] * 2, "--", color="m", alpha=0.5)
    ax.text(x.min(), -12, "f(a)", color="m")

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point."""
    plot_tangent_space_cubic()


if __name__ == "__main__":
    main()
