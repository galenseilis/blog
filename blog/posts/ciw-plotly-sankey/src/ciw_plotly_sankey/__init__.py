"""Plot Ciw's cafe example as a Sankey diagram using Plotly.

The public modules follow the pipeline in the post:

* :mod:`ciw_plotly_sankey.network` -- run the cafe example.
* :mod:`ciw_plotly_sankey.first_nodes` -- count arrivals at the arrival node.
* :mod:`ciw_plotly_sankey.edge_flows` -- count flow along each edge.
* :mod:`ciw_plotly_sankey.combine` -- stack the two flow tables.
* :mod:`ciw_plotly_sankey.sort` -- sort the link table.
* :mod:`ciw_plotly_sankey.figure` -- build the Plotly Sankey figure.
* :mod:`ciw_plotly_sankey.render` -- style the figure and render HTML.
"""

from __future__ import annotations

from ciw_plotly_sankey.network import get_records, run_simulation

__all__ = ["get_records", "run_simulation"]

__version__ = "0.1.0"
