"""Draw each rank permutation as a checkerboard grid.

A permutation ``y`` of the ranks ``x = (1, ..., n)`` is drawn as an ``n x n``
grid: cell ``(i, j)`` is filled when ``y`` maps ``i`` to ``j``. The yellow
squares therefore mark the members of the relation, and every possible sample of
four continuous observations is one of these grids.
"""

from __future__ import annotations

from collections.abc import Sequence
from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

DEFAULT_OUTPUT = "figures/perm_grid.png"
"""Where the post expects the figure to live."""


def spearman_correlation(x: Sequence[float], y: Sequence[float]) -> float:
    """Return the Pearson correlation of two samples.

    Spearman's coefficient is exactly the Pearson correlation of the ranks, so
    this is the function the post's script defined as ``corr``.
    """
    return pearsonr(x, y)[0]


def permutation_grid(
    output: str | Path = "figures/perm_grid.png",
    n: int = 4,
) -> Path:
    """Render every permutation of ``n`` ranks and write the figure.

    Returns the path to the written image.
    """
    fig, axes = plt.subplots(6, 4)
    axes = axes.flatten()

    x = list(range(1, n + 1))
    for ax, y in zip(axes, permutations(x), strict=False):
        img = np.zeros((len(x), len(x)))
        for i, j in zip(x, y):
            img[i - 1, j - 1] = 1
        ax.imshow(img, origin="lower")
        ax.axis("off")

    plt.tight_layout()
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight", dpi=300, transparent=True)
    plt.close(fig)
    return output_path


def main() -> None:
    """Console-script entry point: write the permutation grid figure."""
    permutation_grid()


if __name__ == "__main__":
    main()
