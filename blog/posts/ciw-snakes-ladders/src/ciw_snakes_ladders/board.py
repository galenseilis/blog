"""The Snakes and Ladders board and its routing matrix.

The board is a contiguous sequence of ``n_squares`` tiles labelled ``1`` to
``n_squares``. From a tile that is not the head of a snake or the foot of a
ladder, a player moves forward by an ordinary die roll: one, two, ... six
tiles. These seven tiles, plus the six jump entries, are modelled as a
stochastic (routing) matrix ``R`` where ``R[i][j]`` is the probability of
moving from tile ``i + 1`` to tile ``j + 1``.

Two details are worth calling out:

* Tiles are one-indexed for the reader but zero-indexed in ``R``; the jump
  entries are written with the ``- 1`` offsets so they read like the tile
  labels.
* Every ordinary row must sum to one, otherwise Ciw treats the leftover
  probability as an exit from the system. Near the end of the board a die roll
  can overshoot the final square, so those outcomes are *clamped* onto the
  final square. Without the clamp, tiles 25 to 29 would leak probability mass,
  players would leave the board early, and "reaching the end" would not be
  well defined.
"""

from __future__ import annotations

jump_spots = (7, 10, 14, 23, 24, 28)

n_squares = 30


def build_routing_matrix() -> list[list[float]]:
    """Return the ``30 x 30`` routing matrix for the board.

    Returns
    -------
    list of list of float
        ``R[i][j]`` is the probability of moving from tile ``i + 1`` to tile
        ``j + 1``. Ordinary tiles use a fair six-sided die; jump spots route
        with probability one.
    """
    R = [[0.0] * n_squares for _ in range(n_squares)]

    for i in range(n_squares):
        if i + 1 in jump_spots:
            continue
        if i == n_squares - 1:
            continue
        for step in range(1, 7):
            R[i][min(i + step, n_squares - 1)] += 1 / 6

    R[10 - 1][3 - 1] = 1.0
    R[7 - 1][19 - 1] = 1.0
    R[14 - 1][25 - 1] = 1.0
    R[24 - 1][9 - 1] = 1.0
    R[23 - 1][29 - 1] = 1.0
    R[28 - 1][12 - 1] = 1.0

    return R
