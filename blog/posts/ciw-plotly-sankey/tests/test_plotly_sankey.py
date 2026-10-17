import pandas as pd
import pytest

from ciw_plotly_sankey import figure, network, render
from ciw_plotly_sankey.combine import combine_flows
from ciw_plotly_sankey.edge_flows import edge_flows
from ciw_plotly_sankey.first_nodes import first_nodes
from ciw_plotly_sankey.sort import sort_flows


@pytest.fixture(scope="module")
def records() -> pd.DataFrame:
    simulation = network.run_simulation()
    return network.get_records(simulation)


@pytest.fixture(scope="module")
def links(records: pd.DataFrame) -> pd.DataFrame:
    return render.prepare_links(records)


def test_network_has_expected_nodes(records: pd.DataFrame):
    assert set(records.node.unique()) == {1, 2, 3}


def test_first_nodes_counts_arrivals(records: pd.DataFrame):
    arrivals = first_nodes(records)
    assert list(arrivals.columns) == ["node", "flow"]
    assert set(arrivals.node) == {0}
    assert sorted(arrivals.flow) == [33, 50]


def test_edge_flows_remaps_exit(records: pd.DataFrame):
    edges = edge_flows(records)
    assert list(edges.columns) == ["node", "destination", "flow"]
    assert -1 not in set(edges.destination)


def test_combined_link_table_matches_the_post(links: pd.DataFrame):
    assert list(links.node) == [1, 1, 2, 3, 0, 0]
    assert list(links.flow) == [13, 37, 46, 83, 33, 50]


def test_combined_link_destinations(links: pd.DataFrame):
    destinations = list(links.destination)
    assert destinations[:4] == [2.0, 3.0, 3.0, 4.0]
    assert all(pd.isna(d) for d in destinations[4:])


def test_combine_stacks_frames(records: pd.DataFrame):
    combined = combine_flows(first_nodes(records), edge_flows(records))
    assert len(combined) == len(first_nodes(records)) + len(edge_flows(records))


def test_sort_is_by_destination_then_node_then_flow(links: pd.DataFrame):
    non_null = links.dropna(subset=["destination"])
    assert list(non_null.flow) == [13, 37, 46, 83]


def test_figure_has_sankey_trace(links: pd.DataFrame):
    fig = figure.build_figure(links)
    assert len(fig.data) == 1
    assert fig.data[0].type == "sankey"
    assert list(fig.data[0].node.label) == figure.node_labels


def test_figure_link_arrays(links: pd.DataFrame):
    fig = figure.build_figure(links)
    assert list(fig.data[0].link.source) == [1, 1, 2, 3, 0, 0]
    assert list(fig.data[0].link.value) == [13, 37, 46, 83, 33, 50]


def test_style_figure_sets_backgrounds(links: pd.DataFrame):
    fig = render.style_figure(figure.build_figure(links))
    assert fig.layout.paper_bgcolor == render.transparent_grey
    assert fig.layout.plot_bgcolor == render.transparent_grey


def test_to_html_returns_a_fragment(links: pd.DataFrame):
    html = render.to_html(figure.build_figure(links))
    assert "Plotly.newPlot" in html
    assert "<html" not in html.lower()


def test_build_diagram_returns_a_figure():
    fig = render.build_diagram()
    assert fig.data[0].type == "sankey"


def test_main_prints_html(capsys):
    render.main()
    captured = capsys.readouterr()
    assert "Plotly.newPlot" in captured.out
