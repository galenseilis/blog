"""Small shared numerical helpers for the Fokker-Planck solvers."""

from __future__ import annotations

import numpy as np


def total_variation(p: np.ndarray, q: np.ndarray, spacing: float = 1.0) -> float:
    """Total-variation distance between two densities.

    When ``p`` and ``q`` are normalised mass functions, ``spacing`` is ``1``
    and the result lies in ``[0, 1]`` with ``0`` for identical densities. When
    ``p`` and ``q`` are densities that integrate to one over a grid of cell
    width ``spacing``, pass that width to recover the same scale.
    """
    return 0.5 * float(np.sum(np.abs(p - q))) * spacing
