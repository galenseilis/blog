import math

import pytest

from moose_ellipse.geometry import ellipse, ellipse_foci, polygons


def test_ellipse_area_is_pi_a_b():
    e = ellipse(0, 0, 5, 3, 0)
    assert e.area == pytest.approx(math.pi * 5 * 3, rel=1e-3)


def test_ellipse_is_centred_on_given_point():
    e = ellipse(2.5, -1.5, 4, 2, 30)
    assert e.centroid.x == pytest.approx(2.5, abs=1e-6)
    assert e.centroid.y == pytest.approx(-1.5, abs=1e-6)


def test_ellipse_rotation_preserves_area():
    e = ellipse(0, 0, 5, 3, 0)
    rotated = ellipse(0, 0, 5, 3, 37)
    assert rotated.area == pytest.approx(e.area, rel=1e-6)


def test_ellipse_foci_are_symmetric_about_centre():
    foci = ellipse_foci(0, 0, 5, 3, 0)
    (x1, y1), (x2, y2) = foci
    assert x1 == pytest.approx(-x2)
    assert y1 == pytest.approx(-y2)


def test_ellipse_foci_on_major_axis():
    foci = ellipse_foci(0, 0, 5, 3, 0)
    c = math.sqrt(5**2 - 3**2)
    assert foci[0] == pytest.approx((-c, 0.0))
    assert foci[1] == pytest.approx((c, 0.0))


def test_ellipse_foci_rejects_a_less_than_b():
    with pytest.raises(ValueError, match="a >= b"):
        ellipse_foci(0, 0, 2, 3, 0)


def test_polygons_of_empty_geometry_is_empty_list():
    from shapely.geometry import Polygon

    assert polygons(Polygon()) == []


def test_polygons_wraps_single_polygon():
    e = ellipse(0, 0, 5, 3, 0)
    parts = polygons(e)
    assert len(parts) == 1
