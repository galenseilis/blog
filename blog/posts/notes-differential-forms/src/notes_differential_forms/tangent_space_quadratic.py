"""Plot the tangent space to a parabola at a point.

The curve is ``y = x**2`` and the point is ``(1, 1)``, whose tangent line is
``y = 2x - 1``. The figure marks the point ``p``, the tangent space
``T_pC``, and the pullbacks onto the coordinate axes.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_tangent_space_quadratic(
    output: str | Path = "figures/tangent_space_quadratic.png",
) -> Path:
    """Draw the tangent space to the parabola at ``(1, 1)`` and save it.

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
    ax.set_ylim([-5, 15])
    # Plot of function
    x = np.linspace(-5, 5, num=100)
    y = x**2
    ax.plot(x, y, color="y")
    # Unit tangent vector
    ax.plot([2, 2], [1, 3], "--", color="tab:blue")
    ax.plot([1, 2], [1, 1], "--", color="tab:blue")
    # Tangent space
    ax.plot(x, 2 * x - 1, color="m")
    ax.text(2, 1, r"$T_pC$", color="m")
    ax.scatter(1, 1, color="m")
    ax.text(1, 0, r"$p$", color="m")
    # Pullbacks
    ax.plot([1] * 2, [-5, 1], "--", color="m", alpha=0.5)
    ax.text(1, -5, r"$a$", color="m")
    ax.plot([-5, 1], [1] * 2, "--", color="m", alpha=0.5)
    ax.text(-5, 1, "f(a)", color="m")
    fig.tight_layout()

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point."""
    plot_tangent_space_quadratic()


if __name__ == "__main__":
    main()
