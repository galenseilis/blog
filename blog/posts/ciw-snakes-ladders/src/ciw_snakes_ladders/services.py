"""Service distributions: one unit of time per move, zero for a jump.

In Ciw a service distribution represents the time until a player's next move.
An ordinary move takes one discrete unit of time (``Deterministic(1)``), while
a jump from a snake or ladder happens instantly (``Deterministic(0)``).
"""

from __future__ import annotations

import ciw

from ciw_snakes_ladders.board import jump_spots, n_squares


def build_service_distributions() -> list:
    """Return the per-tile service distributions.

    Returns
    -------
    list
        A length-``n_squares`` list of ``Deterministic`` distributions: zero
        for jump spots and one elsewhere.
    """
    return [
        ciw.dists.Deterministic(0) if i in jump_spots else ciw.dists.Deterministic(1)
        for i in range(n_squares)
    ]
