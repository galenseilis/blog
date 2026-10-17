import matplotlib

matplotlib.use("Agg")

from music_word_adjacency_graph_silent_noon.lyrics import lyrics
from music_word_adjacency_graph_silent_noon.plot_word_adjacency import (
    create_graph,
    plot_word_adjacency,
)


def test_lyrics_is_a_list_of_words():
    assert isinstance(lyrics, list)
    assert lyrics[0] == "your"
    assert lyrics[-1] == "love"
    assert " ".join(lyrics).startswith("your hands lie open")


def test_lyrics_preserves_the_source_text():
    assert "inartciulate" in lyrics
    assert lyrics.count("song") == 3


def test_create_graph_nodes_are_the_words():
    graph = create_graph(lyrics)
    assert set(graph.nodes()) == set(lyrics)
    assert graph.number_of_nodes() == len(set(lyrics))


def test_create_graph_links_consecutive_words():
    graph = create_graph(["a", "b", "c"])
    assert graph.number_of_edges() == 2
    assert graph.has_edge("a", "b")
    assert graph.has_edge("b", "c")


def test_create_graph_collapses_repeated_words():
    graph = create_graph(["a", "b", "a"])
    assert graph.number_of_nodes() == 2
    assert graph.number_of_edges() == 2


def test_plot_word_adjacency_writes_a_png(tmp_path):
    output = tmp_path / "word-adjacency.png"
    written = plot_word_adjacency(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_plot_word_adjacency_creates_parent_directories(tmp_path):
    output = tmp_path / "nested" / "figures" / "word-adjacency.png"
    plot_word_adjacency(output)
    assert output.exists()
