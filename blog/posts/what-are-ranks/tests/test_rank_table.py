from what_are_ranks.rank_table import METHODS, main, rank_table, sample_binomial

EXPECTED = """ x  average method  min method  max method  dense method  ordinal method
 3             1.5         1.0         2.0           1.0             1.0
 3             1.5         1.0         2.0           1.0             2.0
 4             3.0         3.0         3.0           2.0             3.0
 5             4.5         4.0         5.0           3.0             4.0
 5             4.5         4.0         5.0           3.0             5.0
 6             6.5         6.0         7.0           4.0             6.0
 6             6.5         6.0         7.0           4.0             7.0
 7             9.0         8.0        10.0           5.0             8.0
 7             9.0         8.0        10.0           5.0             9.0
 7             9.0         8.0        10.0           5.0            10.0"""


def test_main_prints_expected_table(capsys):
    main()
    assert capsys.readouterr().out == EXPECTED + "\n"


def test_rank_table_has_a_column_per_method():
    table = rank_table(sample_binomial(seed=0))
    assert list(table.columns) == ["x"] + [f"{m} method" for m in METHODS]
    assert len(table) == 10


def test_rank_table_is_sorted_by_sample():
    table = rank_table([5, 3, 5, 1])
    assert list(table["x"]) == [1, 3, 5, 5]


def test_sample_binomial_is_reproducible():
    assert list(sample_binomial(seed=1)) == list(sample_binomial(seed=1))


def test_average_method_preserves_rank_sum():
    table = rank_table([1, 1, 2])
    assert table["average method"].sum() == 6.0
