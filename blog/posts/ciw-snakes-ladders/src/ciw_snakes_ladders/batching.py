"""Batching distributions: all six players arrive at the first tile together.

Batching specifies how many players enter when an arrival occurs. All six enter
at the starting tile, so the first tile has a ``Deterministic(6)`` batch
distribution and the other 29 tiles use ``None`` so that no players arrive
there.
"""

from __future__ import annotations

import ciw

from ciw_snakes_ladders.arrivals import n_players
from ciw_snakes_ladders.board import n_squares


def build_batching_distributions() -> list:
    """Return the per-tile batching distributions.

    Returns
    -------
    list
        A length-``n_squares`` list whose first entry is
        ``ciw.dists.Deterministic(n_players)`` and whose remaining entries are
        ``None``.
    """
    return [ciw.dists.Deterministic(n_players)] + (n_squares - 1) * [None]
