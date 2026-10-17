from dkwm_inequality_sample_size import taylor_series_text


def test_taylor_series_text_contains_expected_terms():
    text = taylor_series_text()
    assert "log" in text
    assert "epsilon" in text
