"""Could two moose have been in the same place at the same time?

Given a pair of fixes per moose (position at the start and at the end of an
interval), a maximum travel speed, and the length of the interval, each moose
gets an ellipse of positions it could have occupied during the interval.

This module:

1. builds those reachable ellipses for two moose,
2. intersects them,
3. asks a stricter question than "do the ellipses overlap": is there a point
   in the overlap where *both* moose could have been present at a *common*
   time?

A moose that starts at ``fix0`` at time ``t0`` and must be at ``fix1`` at time
``t1`` can be at point ``p`` at time ``t`` only if it has enough time to reach
``p`` and still enough time left to reach ``fix1``::

    t0 + |p - fix0| / v  <=  t  <=  t1 - |fix1 - p| / v

So for each moose we get a window of times at which it could have been at ``p``,
and the two moose could have met at ``p`` only if those windows overlap.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry

from moose_ellipse.geometry import ellipse, polygons

Point2D = tuple[float, float]
"""A planar coordinate in kilometres."""


@dataclass(frozen=True)
class Scenario:
    """A single two-moose comparison over a shared time interval."""

    label: str
    fixes_a: tuple[Point2D, Point2D]
    fixes_b: tuple[Point2D, Point2D]
    v_a: float
    v_b: float
    t0: float
    t1: float


def reachable_ellipse(
    fix0: Point2D,
    fix1: Point2D,
    v_max: float,
    dt: float,
) -> BaseGeometry:
    """Positions visitable between two fixes without exceeding ``v_max``.

    ``fix0`` and ``fix1`` are ``(x, y)`` pairs in kilometres, ``v_max`` is in
    kilometres per hour, and ``dt`` is in hours.

    Raises
    ------
    ValueError
        If the fixes are farther apart than the moose could possibly travel
        in ``dt`` hours at ``v_max``.
    """
    (x0, y0), (x1, y1) = fix0, fix1

    separation = math.hypot(x1 - x0, y1 - y0)
    a = v_max * dt / 2

    if 2 * a < separation:
        raise ValueError(
            f"Fixes are {separation:.3f} km apart but the moose can cover at "
            f"most {2 * a:.3f} km in {dt} h at {v_max} km/h."
        )

    b = math.sqrt(a**2 - (separation / 2) ** 2)
    angle = math.degrees(math.atan2(y1 - y0, x1 - x0))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2

    return ellipse(cx, cy, a, b, angle)


def presence_window(
    p: Point2D,
    fix0: Point2D,
    fix1: Point2D,
    v_max: float,
    t0: float,
    t1: float,
) -> tuple[float, float]:
    """Times in ``[t0, t1]`` at which the moose could be at point ``p``."""
    lo = t0 + math.dist(p, fix0) / v_max
    hi = t1 - math.dist(p, fix1) / v_max
    return lo, hi


def simultaneous_points(
    region: BaseGeometry,
    fixes_a: tuple[Point2D, Point2D],
    fixes_b: tuple[Point2D, Point2D],
    v_max_a: float,
    v_max_b: float,
    t0: float,
    t1: float,
    step: float = 0.05,
) -> list[tuple[float, float, float, float]]:
    """Grid ``region`` for points where both presence windows overlap.

    Returns a list of ``(x, y, lo, hi)`` rows, where ``[lo, hi]`` is the
    common time window during which a meeting at ``(x, y)`` is feasible.
    """
    if region.is_empty:
        return []

    minx, miny, maxx, maxy = region.bounds

    points: list[tuple[float, float, float, float]] = []
    for x in np.arange(minx, maxx + step, step):
        for y in np.arange(miny, maxy + step, step):
            p = (x, y)
            if not region.contains(Point(p)):
                continue

            lo_a, hi_a = presence_window(p, fixes_a[0], fixes_a[1], v_max_a, t0, t1)
            lo_b, hi_b = presence_window(p, fixes_b[0], fixes_b[1], v_max_b, t0, t1)

            lo = max(lo_a, lo_b)
            hi = min(hi_a, hi_b)

            if lo <= hi:
                points.append((x, y, lo, hi))

    return points


def plot_scenario(ax: Axes, scenario: Scenario) -> None:
    """Draw one scenario's reachable ellipses and feasible meeting places."""
    fixes_a = scenario.fixes_a
    fixes_b = scenario.fixes_b
    v_a, v_b = scenario.v_a, scenario.v_b
    t0, t1 = scenario.t0, scenario.t1

    e_a = reachable_ellipse(fixes_a[0], fixes_a[1], v_a, t1 - t0)
    e_b = reachable_ellipse(fixes_b[0], fixes_b[1], v_b, t1 - t0)
    overlap = e_a.intersection(e_b)
    simultaneous = simultaneous_points(overlap, fixes_a, fixes_b, v_a, v_b, t0, t1)

    for polygon in polygons(e_a.difference(e_b)):
        x, y = polygon.exterior.xy
        ax.fill(x, y, color="cornflowerblue", alpha=0.65)
    for polygon in polygons(e_b.difference(e_a)):
        x, y = polygon.exterior.xy
        ax.fill(x, y, color="salmon", alpha=0.65)
    for polygon in polygons(overlap):
        x, y = polygon.exterior.xy
        ax.fill(x, y, color="mediumseagreen", alpha=0.85)

    for geometry, color, name in [
        (e_a, "blue", "Moose A reachable"),
        (e_b, "red", "Moose B reachable"),
    ]:
        for polygon in polygons(geometry):
            x, y = polygon.exterior.xy
            ax.plot(x, y, color=color, linewidth=2, label=name)

    if simultaneous:
        pts = np.array([(x, y) for x, y, _, _ in simultaneous])
        ax.scatter(
            pts[:, 0],
            pts[:, 1],
            s=5,
            color="darkgreen",
            alpha=0.55,
            label="Possible meeting place",
            zorder=5,
        )

    for fix in fixes_a:
        ax.scatter(*fix, color="blue", marker="+", s=130, linewidths=2, zorder=10)
    for fix in fixes_b:
        ax.scatter(*fix, color="red", marker="x", s=70, linewidths=2, zorder=10)

    ax.set_aspect("equal", adjustable="box")
    ax.set_title(scenario.label)
    ax.set_xlabel("km")
    ax.set_ylabel("km")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=8)


def default_scenarios() -> list[Scenario]:
    """The three illustrative scenarios used by the blog post."""
    t0, t1 = 0.0, 2.0
    return [
        Scenario(
            label="Overlap with a common time",
            fixes_a=((0.0, 0.0), (5.0, 1.0)),
            fixes_b=((6.0, 0.0), (1.0, 2.0)),
            v_a=6.0,
            v_b=6.0,
            t0=t0,
            t1=t1,
        ),
        Scenario(
            label="Overlap in space but not in time",
            fixes_a=((0.0, 0.0), (9.0, 0.0)),
            fixes_b=((0.0, 9.0), (0.0, 0.0)),
            v_a=5.0,
            v_b=5.0,
            t0=t0,
            t1=t1,
        ),
        Scenario(
            label="No overlap: meeting ruled out",
            fixes_a=((0.0, 0.0), (5.0, 0.0)),
            fixes_b=((0.0, 8.0), (5.0, 8.0)),
            v_a=4.0,
            v_b=4.0,
            t0=t0,
            t1=t1,
        ),
    ]


def summarise(scenario: Scenario) -> dict[str, float | str]:
    """Return the area and verdict statistics for one scenario."""
    e_a = reachable_ellipse(
        scenario.fixes_a[0], scenario.fixes_a[1], scenario.v_a, scenario.t1 - scenario.t0
    )
    e_b = reachable_ellipse(
        scenario.fixes_b[0], scenario.fixes_b[1], scenario.v_b, scenario.t1 - scenario.t0
    )
    overlap = e_a.intersection(e_b)
    simultaneous = simultaneous_points(
        overlap,
        scenario.fixes_a,
        scenario.fixes_b,
        scenario.v_a,
        scenario.v_b,
        scenario.t0,
        scenario.t1,
    )

    result: dict[str, float | str] = {
        "area_a": e_a.area,
        "area_b": e_b.area,
        "overlap_area": overlap.area,
        "n_meeting_places": len(simultaneous),
    }

    if overlap.is_empty:
        result["verdict"] = "no shared place, so no meeting under this v_max"
    elif not simultaneous:
        result["verdict"] = "shared places exist, but never at a shared time"
    else:
        best = max(simultaneous, key=lambda row: row[3] - row[2])
        x, y, lo, hi = best
        result["verdict"] = "meeting feasible"
        result["best_x"] = x
        result["best_y"] = y
        result["best_lo"] = lo
        result["best_hi"] = hi

    return result


def run(output: str | Path = "figures/cooccurrence_feasibility.png") -> Path:
    """Render the three-scenario figure and return the written path."""
    scenarios = default_scenarios()

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for ax, scenario in zip(axes, scenarios, strict=True):
        plot_scenario(ax, scenario)
        result = summarise(scenario)

        print(f"\n{scenario.label}")
        print(f"  Moose A ellipse area: {result['area_a']:9.3f} km^2")
        print(f"  Moose B ellipse area: {result['area_b']:9.3f} km^2")
        print(f"  Overlap area:         {result['overlap_area']:9.3f} km^2")

        if result["verdict"] == "meeting feasible":
            print(f"  Candidate meeting places on grid: {result['n_meeting_places']}")
            print(
                f"  Widest window at ({result['best_x']:.2f}, {result['best_y']:.2f}) "
                f"km: t in [{result['best_lo']:.3f}, {result['best_hi']:.3f}] h"
            )
        else:
            print(f"  Verdict: {result['verdict']}")

    fig.suptitle(
        "Reachable ellipses for two moose over t in [0, 2] h under three assumptions"
    )
    fig.tight_layout()

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"\nSaved plot to: {output_path}")
    return output_path


def main() -> None:
    """Console-script entry point."""
    run()


if __name__ == "__main__":
    main()
