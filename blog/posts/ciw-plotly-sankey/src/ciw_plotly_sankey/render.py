"""Style the figure and render it to embeddable HTML.

This is the last step of the pipeline: run the cafe example, build the link
table, draw the Sankey figure, set the paper and plot backgrounds, and print
the figure as an HTML fragment ready to paste into a post.
"""

from __future__ import annotations

import plotly.graph_objects as go

from ciw_plotly_sankey.combine import combine_flows
from ciw_plotly_sankey.edge_flows import edge_flows
from ciw_plotly_sankey.figure import build_figure
from ciw_plotly_sankey.first_nodes import first_nodes
from ciw_plotly_sankey.network import get_records, run_simulation
from ciw_plotly_sankey.sort import sort_flows

transparent_grey = "rgba(0.5,0.5,0.5,0.5)"


def prepare_links(recs) -> "object":
    """Turn the simulation records into the sorted Sankey link table."""
    arrival_flows = first_nodes(recs)
    flow_edges = edge_flows(recs)
    return sort_flows(combine_flows(arrival_flows, flow_edges))


def style_figure(fig: go.Figure) -> go.Figure:
    """Set the paper and plot backgrounds of the figure."""
    fig.layout.paper_bgcolor = transparent_grey
    fig.layout.plot_bgcolor = transparent_grey
    return fig


def to_html(fig: go.Figure) -> str:
    """Return the figure as an HTML fragment using the Plotly CDN."""
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


def build_diagram() -> go.Figure:
    """Run the cafe example and return the styled Sankey figure."""
    simulation = run_simulation()
    recs = get_records(simulation)
    return style_figure(build_figure(prepare_links(recs)))


def main() -> None:
    """Build the diagram and print its HTML representation."""
    print(to_html(build_diagram()))


if __name__ == "__main__":
    main()
