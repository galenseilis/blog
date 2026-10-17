from spearman_correlation.permutations import (
    permutation_table,
    rank_columns,
    rank_permutations,
)


def test_rank_permutations_count():
    assert len(rank_permutations(4)) == 24


def test_rank_permutations_are_permutations():
    for perm in rank_permutations(4):
        assert sorted(perm) == [1, 2, 3, 4]


def test_rank_columns_are_latex_labels():
    cols = rank_columns(3)
    assert cols == [
        "$\\operatorname{rank}(X_1)$",
        "$\\operatorname{rank}(X_2)$",
        "$\\operatorname{rank}(X_3)$",
    ]


def test_permutation_table_has_header_and_rows():
    table = permutation_table(4)
    assert "$\\operatorname{rank}(X_1)$" in table
    assert len([line for line in table.splitlines() if line.strip()]) == 26
