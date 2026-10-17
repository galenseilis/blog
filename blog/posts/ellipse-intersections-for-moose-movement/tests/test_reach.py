import math

import numpy as np
import pytest
from shapely.geometry import Point

from moose_ellipse.reach import (
    Scenario,
    default_scenarios,
    presence_window,
    reachable_ellipse,
    simultaneous_points,
    summarise,
)


def test_reachable_ellipse_foci_are_the_two_fixes():
    fix0, fix1 = (0.0, 0.0), (5.0, 1.0)
    v_max, dt = 6.0, 2.0
    e = reachable_ellipse(fix0, fix1, v_max, dt)
    # The defining property: every boundary point has distance sum 2a to the
    # two fixes, which is exactly the statement that the fixes are the foci.
    coords = np.array(e.exterior.coords)
    summed = np.hypot(coords[:, 0] - fix0[0], coords[:, 1] - fix0[1]) + np.hypot(
        coords[:, 0] - fix1[0], coords[:, 1] - fix1[1]
    )
    assert np.allclose(summed, v_max * dt, rtol=1e-3)


def test_reachable_ellipse_area_matches_semi_axes():
    fix0, fix1 = (0.0, 0.0), (5.0, 1.0)
    v_max, dt = 6.0, 2.0
    e = reachable_ellipse(fix0, fix1, v_max, dt)
    separation = math.hypot(1.0, 5.0)
    a = v_max * dt / 2
    b = math.sqrt(a**2 - (separation / 2) ** 2)
    assert e.area == pytest.approx(math.pi * a * b, rel=1e-3)


def test_reachable_ellipse_raises_when_fixes_infeasible():
    with pytest.raises(ValueError, match="can cover at most"):
        reachable_ellipse((0.0, 0.0), (100.0, 0.0), v_max=1.0, dt=1.0)


def test_reachable_ellipse_is_a_circle_when_fixes_coincide():
    e = reachable_ellipse((3.0, 4.0), (3.0, 4.0), v_max=2.0, dt=2.0)
    assert e.area == pytest.approx(math.pi * 2.0**2, rel=1e-3)


def test_presence_window_endpoints():
    lo, hi = presence_window((0.0, 0.0), (0.0, 0.0), (10.0, 0.0), v_max=5.0, t0=0.0, t1=2.0)
    assert lo == pytest.approx(0.0)
    assert hi == pytest.approx(2.0 - 2.0)


def test_simultaneous_points_empty_region_returns_empty():
    from shapely.geometry import Polygon

    result = simultaneous_points(
        Polygon(), ((0.0, 0.0), (1.0, 0.0)), ((0.0, 0.0), (1.0, 0.0)), 5.0, 5.0, 0.0, 1.0
    )
    assert result == []


def test_default_scenarios_are_ordered_by_verdict():
    verds = [summarise(s)["verdict"] for s in default_scenarios()]
    assert verds[0] == "meeting feasible"
    assert "never at a shared time" in verds[1]
    assert "no shared place" in verds[2]


def test_summarise_reports_meeting_place_for_feasible_scenario():
    scenario = Scenario(
        label="feasible",
        fixes_a=((0.0, 0.0), (5.0, 1.0)),
        fixes_b=((6.0, 0.0), (1.0, 2.0)),
        v_a=6.0,
        v_b=6.0,
        t0=0.0,
        t1=2.0,
    )
    result = summarise(scenario)
    assert result["verdict"] == "meeting feasible"
    assert result["n_meeting_places"] > 0
    assert result["best_lo"] <= result["best_hi"]
