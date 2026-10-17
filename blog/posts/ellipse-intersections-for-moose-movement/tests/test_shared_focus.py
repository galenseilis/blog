import math

import pytest
from shapely.geometry import Point

from moose_ellipse.shared_focus import EllipseSpec, build_shared_focus_demo


def test_shared_focus_construction_second_ellipse_passes_through_focus():
    demo = build_shared_focus_demo()
    # The shared focus is a focus of the first ellipse.
    assert demo.foci1[0] == pytest.approx(demo.shared_focus)
    # ...and one of the foci of the second ellipse.
    assert any(
        math.isclose(fx, demo.shared_focus[0], abs_tol=1e-9)
        and math.isclose(fy, demo.shared_focus[1], abs_tol=1e-9)
        for fx, fy in demo.foci2
    )


def test_shared_focus_is_inside_both_ellipses():
    demo = build_shared_focus_demo()
    focus = Point(demo.shared_focus)
    assert demo.e1.covers(focus)
    assert demo.e2.covers(focus)


def test_areas_partition_the_two_ellipses():
    demo = build_shared_focus_demo()
    assert demo.e1_only.area + demo.intersection.area == pytest.approx(
        demo.e1.area, rel=1e-6
    )
    assert demo.e2_only.area + demo.intersection.area == pytest.approx(
        demo.e2.area, rel=1e-6
    )


def test_ellipse_area_is_pi_a_b():
    demo = build_shared_focus_demo(EllipseSpec(0, 0, 5, 3, 0))
    assert demo.e1.area == pytest.approx(math.pi * 5 * 3, rel=1e-3)
