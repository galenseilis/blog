import numpy as np
import pytest

from moose_fp.beyond_gaussian_fp import (
    advance_periodic,
    flow_contract,
    fractional_ou,
    interaction_run,
    sample_path,
    self_consistent_variance,
    switch_run,
)


def test_flow_contract_conserves_mass():
    x = np.linspace(-8.0, 8.0, 256, endpoint=False)
    p = np.exp(-0.5 * x**2)
    p /= p.sum()
    moved = flow_contract(p, x, a=1.01)
    assert moved.sum() == pytest.approx(p.sum(), rel=1e-9)
    assert np.all(moved >= 0.0)


def test_advance_periodic_conserves_mass_and_nonnegative():
    x = np.linspace(-8.0, 8.0, 256, endpoint=False)
    spacing = x[1] - x[0]
    p = np.exp(-0.5 * x**2)
    p /= p.sum()
    p_next = advance_periodic(p, -x, spacing, diffusion=1.0, dt=1e-4)
    assert p_next.sum() == pytest.approx(p.sum(), rel=1e-9)
    assert np.all(p_next >= 0.0)


def test_self_consistent_variance_without_interaction_is_d_over_kappa():
    assert self_consistent_variance(0.0, width=0.5) == pytest.approx(1.0)


def test_self_consistent_variance_with_interaction_is_smaller():
    assert self_consistent_variance(0.6, width=0.5) < self_consistent_variance(0.0, 0.5)


def test_fractional_ou_returns_normalised_density():
    x, p, spacing, _drift = fractional_ou(alpha=1.0, n_steps=200, dt=0.005, grid=256, length=32.0)
    assert x.shape == p.shape
    assert np.sum(p) * spacing == pytest.approx(1.0, rel=1e-3)
    # The Fourier step leaves only round-off-level negatives.
    assert p.min() > -1e-8


def test_interaction_run_without_interaction_returns_density():
    # dt is chosen below the explicit stability limit 0.2 * spacing**2 / D.
    x, p, t, _change = interaction_run(0.0, grid=128, length=16.0, dt=0.002, t_end=0.2, width=0.5)
    assert x.shape == p.shape
    assert p.sum() == pytest.approx(1.0, rel=1e-6)
    assert t > 0.0


def test_switch_run_tracks_mass_in_two_states():
    grid_s, length_s = 128, 16.0
    spacing_s = length_s / grid_s
    x_s = -0.5 * length_s + np.arange(grid_s) * spacing_s
    dt_s = 0.25 * spacing_s**2 / 0.60
    snapshots = switch_run(x_s, spacing_s, dt_s, 5.0, snapshot_at=(5.0,))
    p_a, p_b = snapshots[5.0]
    assert (p_a.sum() + p_b.sum()) == pytest.approx(1.0, rel=1e-6)


def test_sample_path_shapes_and_binary_states():
    times, position, states = sample_path(0.01, 2.0)
    assert times.shape == position.shape == states.shape
    assert set(np.unique(states)).issubset({0, 1})
