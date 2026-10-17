import numpy as np

from moose_fp.numerics import total_variation


def test_total_variation_identical_is_zero():
    p = np.array([0.25, 0.25, 0.25, 0.25])
    assert total_variation(p, p) == 0.0


def test_total_variation_disjoint_is_one():
    p = np.array([0.5, 0.5, 0.0, 0.0])
    q = np.array([0.0, 0.0, 0.5, 0.5])
    assert total_variation(p, q) == 1.0


def test_total_variation_half_overlap():
    p = np.array([0.5, 0.5])
    q = np.array([1.0, 0.0])
    assert total_variation(p, q) == 0.5


def test_total_variation_spacing_scales():
    p = np.array([0.25, 0.25, 0.25, 0.25])
    q = np.array([0.5, 0.5, 0.0, 0.0])
    base = total_variation(p, q)
    assert total_variation(p, q, spacing=2.0) == 2.0 * base
