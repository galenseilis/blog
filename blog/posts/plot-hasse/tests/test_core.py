from plot_hasse import factors, make_graph, plot_hasse, pos_hasse


def test_factors_of_6():
    assert factors(6) == {1, 2, 3, 6}


def test_make_graph_has_correct_edges():
    g = make_graph(6)
    assert 1 in g
    assert 6 in g


def test_plot_hasse_creates_file(tmp_path):
    out = tmp_path / "diagram.png"
    result = plot_hasse(n=6, output_path=str(out))
    assert result == str(out)
    assert out.exists()
