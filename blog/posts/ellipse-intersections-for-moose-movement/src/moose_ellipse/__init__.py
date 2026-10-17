"""Reachable-ellipse geometry for moose movement between two GPS fixes.

The public helpers live in :mod:`moose_ellipse.geometry`,
:mod:`moose_ellipse.reach`, and :mod:`moose_ellipse.shared_focus`:

* :func:`moose_ellipse.reach.reachable_ellipse` builds the potential path
  area for a single animal between two fixes.
* :func:`moose_ellipse.reach.simultaneous_points` grids a spatial overlap for
  places and times at which two animals could actually have met.
* :func:`moose_ellipse.shared_focus.ellipse_foci` returns the foci of an
  arbitrarily oriented ellipse.
"""

from __future__ import annotations

from moose_ellipse.geometry import ellipse, ellipse_foci, polygons

__all__ = [
    "ellipse",
    "ellipse_foci",
    "polygons",
]

__version__ = "0.1.0"
