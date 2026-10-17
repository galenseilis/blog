"""Number of servers: unlimited, so players never block one another.

A server at a tile controls how many players can leave that tile at once.
Assigning ``float("inf")`` to every tile means there is no limit, so pieces
cannot block each other. The queueing aspect of Ciw is therefore unimportant
here, which is why the queue capacity is left at its (infinite) default.
"""

from __future__ import annotations

from ciw_snakes_ladders.board import n_squares


def build_number_of_servers() -> list:
    """Return an infinite number of servers for every tile.

    Returns
    -------
    list
        A length-``n_squares`` list of ``float('inf')``.
    """
    return [float("inf")] * n_squares
