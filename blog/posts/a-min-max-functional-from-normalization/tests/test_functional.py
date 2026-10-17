from a_min_max_functional_from_normalization.functional import generate_functional_table


def test_generate_table_has_expected_columns():
    df = generate_functional_table()
    assert list(df.columns) == ["f", "g", "Functional"]
    assert len(df) == 36  # 6x6
