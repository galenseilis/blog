from music_word_adjacency_rolling_down_to_rio import create_graph, lyrics


def test_create_graph_has_nodes():
    G = create_graph(lyrics)
    assert G.number_of_nodes() == len(set(lyrics))
