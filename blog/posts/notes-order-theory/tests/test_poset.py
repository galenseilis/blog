import matplotlib

matplotlib.use("Agg")

import networkx as nx

from notes_order_theory import (
    COVER_EDGES,
    EXAMPLE_ORDER,
    build_cover_graph,
    build_digraph,
    plot_cover_diagram,
    plot_example_partial_order,
)
from notes_order_theory.figures import render_all


def test_build_digraph_nodes_and_edges():
    graph = build_digraph()
    assert set(graph.nodes()) == {"a", "b", "c", "d", "e"}
    assert graph.number_of_edges() == len(EXAMPLE_ORDER)
    assert graph.has_edge("a", "a")
    assert graph.has_edge("b", "e")


def test_build_digraph_accepts_custom_order():
    graph = build_digraph(["ab", "bc"])
    assert graph.number_of_edges() == 2
    assert graph.has_edge("a", "b")
    assert graph.has_edge("b", "c")


def test_build_cover_graph_edges():
    graph = build_cover_graph()
    assert {frozenset(edge) for edge in graph.edges()} == {
        frozenset(edge) for edge in COVER_EDGES
    }
    assert not graph.has_edge("b", "e")


def test_plot_example_partial_order_writes_a_png(tmp_path):
    output = tmp_path / "partial_order.png"
    written = plot_example_partial_order(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_plot_cover_diagram_writes_a_png(tmp_path):
    output = tmp_path / "cover.png"
    written = plot_cover_diagram(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_render_all_writes_every_post_figure(tmp_path):
    paths = render_all(tmp_path)
    assert [path.name for path in paths] == [
        "example_partial_order.png",
        "cover_diagram.png",
    ]
    assert all(path.exists() for path in paths)


def test_plot_functions_create_parent_directories(tmp_path):
    output = tmp_path / "nested" / "deeper" / "cover.png"
    plot_cover_diagram(output)
    assert output.exists()
