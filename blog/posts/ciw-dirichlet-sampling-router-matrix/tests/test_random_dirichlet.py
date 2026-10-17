import numpy as np
import pytest

from ciw_dirichlet_sampling_router_matrix import RandomDirichletList


def test_sum_to_one():
    rdl = RandomDirichletList([1, 2, 3])
    assert pytest.approx(sum(rdl), abs=1e-10) == 1.0


def test_len_matches_alphas():
    rdl = RandomDirichletList([1, 2, 3, 4])
    assert len(rdl) == 4


def test_min_max_in_range():
    rdl = RandomDirichletList([1, 2, 3])
    assert 0 <= rdl.__min__() <= 1
    assert 0 <= rdl.__max__() <= 1


def test_getitem_returns_float():
    rdl = RandomDirichletList([1, 2, 3])
    v = rdl[0]
    assert isinstance(v, float)


def test_positive_alphas_required():
    with pytest.raises(ValueError):
        RandomDirichletList([1, -1, 3])
