from music_word_adjacency_the_little_irish_girl import lyrics


def test_lyrics_is_list():
    assert isinstance(lyrics, list)
    assert len(lyrics) > 0
