"""Arrival distributions: all six players enter once, at time zero.

New arrivals only occur once, at the very beginning of the simulation, and all
six players enter at the first tile. Every other tile therefore has an arrival
distribution of ``None`` (written compactly as ``29 * [None]``). The first tile
uses a sequential distribution whose first arrival is at time ``0`` and whose
second arrival is at infinity, so no further arrivals ever occur.
"""

from __future__ import annotations

import ciw

from ciw_snakes_ladders.board import n_squares

n_players = 6


def build_arrival_distributions() -> list:
    """Return the per-tile arrival distributions.

    Returns
    -------
    list
        A length-``n_squares`` list whose first entry is
        ``ciw.dists.Sequential([0, inf])`` and whose remaining entries are
        ``None``.
    """
    return [ciw.dists.Sequential([0, float("inf")])] + (n_squares - 1) * [None]
