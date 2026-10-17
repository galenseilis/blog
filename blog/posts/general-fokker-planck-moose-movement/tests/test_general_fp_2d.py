import numpy as np
import pytest

from moose_fp.general_fp_2d import (
    D0,
    GRID,
    LENGTH,
    build_domain,
    centre_delta,
    solve,
    steady_state,
)


def test_build_domain_shapes_and_river():
    x, y, xx, yy, potential, solid = build_domain()
    assert xx.shape == (GRID, GRID)
    assert potential.shape == (GRID, GRID)
    # The river is a wall at x = 2 km, except at the bridge near y = 0.7 km.
    wall_col = np.isclose(x, 2.0, atol=0.75 * (x[1] - x[0]))
    assert solid[wall_col, :].any()
    bridge_row = np.isclose(y, 0.7, atol=0.5 * (y[1] - y[0]))
    assert not solid[np.ix_(wall_col, bridge_row)].all()
    # Two habitat wells make the potential negative near (1, 2) and (3, 2).
    assert potential.min() < -0.5


def test_steady_state_is_normalised_and_zero_on_solid():
    _x, _y, _xx, _yy, potential, solid = build_domain()
    p = steady_state(potential, solid, D0)
    assert p.sum() == pytest.approx(1.0)
    assert np.all(p[solid] == 0.0)
    assert np.all(p >= 0.0)


def test_centre_delta_is_normalised_point_mass():
    x = np.linspace(0.0, LENGTH, GRID)
    y = np.linspace(0.0, LENGTH, GRID)
    solid = np.zeros((GRID, GRID), dtype=bool)
    p = centre_delta(x, y, 1.0, 2.0, solid)
    assert p.sum() == pytest.approx(1.0)
    assert p.max() == pytest.approx(1.0)


def test_solve_conserves_mass_and_stays_nonnegative():
    x, y, _xx, _yy, potential, solid = build_domain()
    p0 = centre_delta(x, y, 1.0, 2.0, solid)
    p, _dt, _saved, _open = solve(potential, solid, D0, p0, 1.0)
    assert p.sum() == pytest.approx(p0.sum(), rel=1e-6)
    assert np.all(p >= 0.0)
    assert np.all(p[solid] == 0.0)


def test_solve_records_requested_times():
    x, y, _xx, _yy, potential, solid = build_domain()
    p0 = centre_delta(x, y, 1.0, 2.0, solid)
    record = (0.1, 0.2, 0.3)
    _p, _dt, saved, _open = solve(
        potential, solid, D0, p0, 1.0, record_times=record
    )
    assert set(saved) == set(record)
