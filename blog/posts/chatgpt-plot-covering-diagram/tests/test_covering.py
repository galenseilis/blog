import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx

from chatgpt_plot_covering_diagram import covering_diagram
from chatgpt_plot_covering_diagram.failing_example import failing_example
from chatgpt_plot_covering_diagram.full_example import full_example


def test_covering_diagram_returns_axes():
    dg = nx.DiGraph()
    dg.add_edges_from([("a", "b"), ("b", "c")])
    ax = covering_diagram(dg)
    assert isinstance(ax, matplotlib.axes.Axes)
    plt.close(ax.figure)


def test_covering_diagram_uses_supplied_axes():
    dg = nx.DiGraph()
    dg.add_edges_from([("a", "b")])
    fig, ax = plt.subplots()
    returned = covering_diagram(dg, ax=ax)
    assert returned is ax
    plt.close(fig)


def test_covering_diagram_labels_every_node():
    dg = nx.DiGraph()
    dg.add_edges_from([("a", "b"), ("b", "c"), ("a", "c")])
    ax = covering_diagram(dg)
    labels = {text.get_text() for text in ax.texts}
    assert labels == {"a", "b", "c"}
    plt.close(ax.figure)


def test_covering_diagram_turns_off_the_axis():
    dg = nx.DiGraph()
    dg.add_edges_from([("a", "b")])
    ax = covering_diagram(dg)
    assert not ax.axison
    plt.close(ax.figure)


def test_full_example_writes_a_png(tmp_path):
    output = tmp_path / "figures" / "full.png"
    written = full_example(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_failing_example_writes_a_png(tmp_path):
    output = tmp_path / "figures" / "failing.png"
    written = failing_example(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0
