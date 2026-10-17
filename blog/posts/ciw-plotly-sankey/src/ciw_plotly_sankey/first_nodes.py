"""Count how many customers first entered at each node.

Ciw's records do not include the arrival node, so to draw the flow out of the
arrival node we find, for each customer, the first node they visited and count
how many customers started at each node. Those counts are returned with
``node == 0``, the index used for the arrival node in the Sankey diagram.
"""

from __future__ import annotations

import pandas as pd


def first_nodes(recs: pd.DataFrame) -> pd.DataFrame:
    """Return the number of customers whose first node was each node.

    Parameters
    ----------
    recs:
        The records table from a Ciw simulation.

    Returns
    -------
    pandas.DataFrame
        A frame with columns ``node`` (always ``0``, the arrival node) and
        ``flow`` (the number of customers that first arrived at each node).
    """
    return (
        recs.sort_values(by="arrival_date")
        .groupby("id_number")["node"]
        .apply(lambda x: x.iloc[0])
        .value_counts()
        .reset_index(name="flow")
        .rename(columns={"index": "destination"})
        .assign(node=0)
    )
