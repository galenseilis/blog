"""Build the Plotly Sankey figure from the link table.

The nodes are labelled ``ArrivalNode``, ``ColdFood``, ``HotFood``, ``Till``,
and ``Exit`` -- indices ``0`` to ``4`` -- matching the ``node`` and
``destination`` indices in the link table.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

node_labels = ["ArrivalNode", "ColdFood", "HotFood", "Till", "Exit"]


def build_figure(recs: pd.DataFrame) -> go.Figure:
    """Return a Plotly Sankey figure for the link table.

    Parameters
    ----------
    recs:
        A link table with columns ``node``, ``destination``, and ``flow``.

    Returns
    -------
    plotly.graph_objects.Figure
        The Sankey figure.
    """
    return go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(label=node_labels, pad=10),
            link=dict(
                arrowlen=15,
                source=recs.node,
                target=recs.destination,
                value=recs.flow,
            ),
        )
    )
