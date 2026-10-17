from music_word_adjacency_rolling_down_to_rio import lyrics


def test_lyrics_is_list():
    assert isinstance(lyrics, list)
    assert len(lyrics) > 0
    for word in lyrics:
        assert isinstance(word, str)
