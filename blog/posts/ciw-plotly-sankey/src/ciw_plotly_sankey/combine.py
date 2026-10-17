"""Combine the arrival and edge flow tables into one link table.

The arrival-node flows and the edge flows share the columns ``node`` and
``flow`` (the edge table additionally has ``destination``), so they can simply
be stacked with :func:`pandas.concat` to form the complete set of Sankey links.
"""

from __future__ import annotations

import pandas as pd


def combine_flows(
    arrival_flows: pd.DataFrame, edge_flows: pd.DataFrame
) -> pd.DataFrame:
    """Stack the arrival flows and the edge flows.

    Parameters
    ----------
    arrival_flows:
        The frame returned by
        :func:`ciw_plotly_sankey.first_nodes.first_nodes`.
    edge_flows:
        The frame returned by
        :func:`ciw_plotly_sankey.edge_flows.edge_flows`.

    Returns
    -------
    pandas.DataFrame
        The concatenation of the two frames.
    """
    return pd.concat((arrival_flows, edge_flows))
