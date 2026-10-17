"""A discrete-event simulation generalization of Snakes and Ladders using Ciw.

The public modules are:

* :mod:`ciw_snakes_ladders.board` -- the tile sequence and routing matrix.
* :mod:`ciw_snakes_ladders.arrivals` -- the once-only arrivals.
* :mod:`ciw_snakes_ladders.services` -- the one-unit and zero-unit move times.
* :mod:`ciw_snakes_ladders.batching` -- the six-player batch at the start.
* :mod:`ciw_snakes_ladders.servers` -- the unlimited number of servers.
* :mod:`ciw_snakes_ladders.simulate` -- assembling the network and running the
  game to a winner.
"""

from __future__ import annotations

from ciw_snakes_ladders.simulate import (
    build_network,
    main,
    run_simulation,
    winner,
)

__all__ = ["build_network", "main", "run_simulation", "winner"]

__version__ = "0.1.0"
