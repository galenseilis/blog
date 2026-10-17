"""Count the flow along every edge of the network.

Grouping the records by ``(node, destination)`` and counting gives the number
of moves along each edge. Customers leaving the system are recorded with a
destination of ``-1``; that is remapped to the index used for the exit node
(``4``) so that the Sankey diagram can draw them.
"""

from __future__ import annotations

import pandas as pd

exit_index = 4


def edge_flows(recs: pd.DataFrame, exit_node: int = exit_index) -> pd.DataFrame:
    """Return the number of moves along each edge.

    Parameters
    ----------
    recs:
        The records table from a Ciw simulation.
    exit_node:
        The index to use for the exit node, replacing Ciw's ``-1``.

    Returns
    -------
    pandas.DataFrame
        A frame with columns ``node``, ``destination``, and ``flow``.
    """
    return (
        recs.groupby(by=["node", "destination"])
        .size()
        .reset_index(name="flow")
        .replace({-1: exit_node})
    )
