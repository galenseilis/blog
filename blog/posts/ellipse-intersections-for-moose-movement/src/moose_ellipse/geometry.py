"""Low-level ellipse construction and Shapely polygon helpers.

An ellipse is built by buffering the origin to a unit disc and then scaling,
rotating, and translating it, so that arbitrary orientation is handled by
Shapely's affine transforms rather than by hand-rolling the conic.
"""

from __future__ import annotations

import math
from collections.abc import Iterable

import matplotlib.axes
from shapely.affinity import rotate, scale, translate
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry


def ellipse(
    cx: float,
    cy: float,
    a: float,
    b: float,
    angle_deg: float,
    resolution: int = 256,
) -> BaseGeometry:
    """Return a Shapely ellipse centred at ``(cx, cy)``.

    Parameters
    ----------
    cx, cy:
        Centre of the ellipse.
    a:
        Semi-major axis length (``a >= b``).
    b:
        Semi-minor axis length.
    angle_deg:
        Rotation of the major axis, in degrees counter-clockwise.
    resolution:
        Number of segments per quadrant used to approximate the boundary.
    """
    geometry = Point(0, 0).buffer(1, quad_segs=resolution)
    geometry = scale(geometry, a, b)
    geometry = rotate(geometry, angle_deg, origin=(0, 0))
    return translate(geometry, cx, cy)


def ellipse_foci(
    cx: float,
    cy: float,
    a: float,
    b: float,
    angle_deg: float,
) -> list[tuple[float, float]]:
    """Return the two foci of an arbitrarily oriented ellipse.

    Parameters
    ----------
    cx, cy:
        Centre of the ellipse.
    a, b:
        Semi-major and semi-minor axis lengths, with ``a >= b``.
    angle_deg:
        Rotation of the major axis, in degrees counter-clockwise.

    Raises
    ------
    ValueError
        If ``a < b``.
    """
    if a < b:
        raise ValueError("This function expects a >= b.")

    focal_distance = math.sqrt(a**2 - b**2)
    theta = math.radians(angle_deg)
    dx = focal_distance * math.cos(theta)
    dy = focal_distance * math.sin(theta)

    return [
        (cx - dx, cy - dy),
        (cx + dx, cy + dy),
    ]


def polygons(geometry: BaseGeometry) -> list[BaseGeometry]:
    """Return the polygonal parts of ``geometry`` as a list.

    Shapely set operations can return a ``Polygon`` or a multi-part
    ``MultiPolygon`` (or an empty geometry). This normalises the result so
    callers can always iterate.
    """
    if geometry.is_empty:
        return []
    if geometry.geom_type == "Polygon":
        return [geometry]
    return list(geometry.geoms)


def plot_geometry(
    geometry: BaseGeometry,
    ax: matplotlib.axes.Axes,
    **kwargs: object,
) -> None:
    """Fill every polygonal part of ``geometry`` on ``ax``."""
    for polygon in polygons(geometry):
        x, y = polygon.exterior.xy
        ax.fill(x, y, **kwargs)


def plot_boundary(
    geometry: BaseGeometry,
    ax: matplotlib.axes.Axes,
    **kwargs: object,
) -> None:
    """Draw the boundary of every polygonal part of ``geometry`` on ``ax``."""
    for polygon in polygons(geometry):
        x, y = polygon.exterior.xy
        ax.plot(x, y, **kwargs)


def points_array(points: Iterable[tuple[float, float]]) -> list[tuple[float, float]]:
    """Materialise an iterable of coordinate pairs (identity, for clarity)."""
    return [(float(x), float(y)) for x, y in points]
