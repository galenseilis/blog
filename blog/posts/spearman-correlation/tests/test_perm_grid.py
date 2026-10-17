import matplotlib

matplotlib.use("Agg")

import pytest

from spearman_correlation.perm_grid import (
    permutation_grid,
    spearman_correlation,
)


def test_spearman_correlation_monotone_is_one():
    assert spearman_correlation([1, 2, 3, 4], [10, 20, 30, 40]) == pytest.approx(1.0)


def test_spearman_correlation_antimonotone_is_minus_one():
    assert spearman_correlation([1, 2, 3, 4], [4, 3, 2, 1]) == pytest.approx(-1.0)


def test_permutation_grid_writes_file(tmp_path):
    output = tmp_path / "figures" / "perm_grid.png"
    written = permutation_grid(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0
