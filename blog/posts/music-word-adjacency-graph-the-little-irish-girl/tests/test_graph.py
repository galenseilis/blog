from music_word_adjacency_the_little_irish_girl import create_graph, lyrics


def test_create_graph_has_nodes():
    G = create_graph(lyrics)
    assert G.number_of_nodes() == len(set(lyrics))
