"""Could two moose have been in the same place at the same time?

Given a pair of fixes per moose (position at the start and at the end of an
interval), a maximum travel speed, and the length of the interval, each moose
gets an ellipse of positions it could have occupied during the interval.

This script:

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

Three scenarios are reported:

* an overlap that also supports a common time,
* an overlap that exists in space but never in time,
* no overlap at all, so a meeting is ruled out under that speed assumption.
"""

import math

import matplotlib.pyplot as plt
import numpy as np

from shapely.affinity import rotate, scale, translate
from shapely.geometry import Point


def ellipse(cx, cy, a, b, angle_deg, resolution=256):
    e = Point(0, 0).buffer(1, quad_segs=resolution)
    e = scale(e, a, b)
    e = rotate(e, angle_deg, origin=(0, 0))
    e = translate(e, cx, cy)
    return e


def reachable_ellipse(fix0, fix1, v_max, dt):
    """Positions visitable between two fixes without exceeding ``v_max``.

    ``fix0`` and ``fix1`` are (x, y) pairs in kilometres, ``v_max`` is in
    kilometres per hour, and ``dt`` is in hours.
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


def presence_window(p, fix0, fix1, v_max, t0, t1):
    """Times in [t0, t1] at which the moose could be at point ``p``."""
    lo = t0 + math.dist(p, fix0) / v_max
    hi = t1 - math.dist(p, fix1) / v_max
    return lo, hi


def simultaneous_points(region, fixes_a, fixes_b, v_max_a, v_max_b, t0, t1, step=0.05):
    """Grid the overlap region for points where both presence windows overlap."""
    if region.is_empty:
        return []

    minx, miny, maxx, maxy = region.bounds

    points = []
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


def polygons(geometry):
    if geometry.is_empty:
        return []
    if geometry.geom_type == "Polygon":
        return [geometry]
    return list(geometry.geoms)


def plot_scenario(ax, scenario):
    fixes_a = scenario["fixes_a"]
    fixes_b = scenario["fixes_b"]
    v_a, v_b = scenario["v_a"], scenario["v_b"]
    t0, t1 = scenario["t0"], scenario["t1"]

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
    ax.set_title(scenario["label"])
    ax.set_xlabel("km")
    ax.set_ylabel("km")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=8)


def main():
    t0, t1 = 0.0, 2.0

    scenarios = [
        {
            "label": "Overlap with a common time",
            "fixes_a": ((0.0, 0.0), (5.0, 1.0)),
            "fixes_b": ((6.0, 0.0), (1.0, 2.0)),
            "v_a": 6.0,
            "v_b": 6.0,
            "t0": t0,
            "t1": t1,
        },
        {
            "label": "Overlap in space but not in time",
            "fixes_a": ((0.0, 0.0), (9.0, 0.0)),
            "fixes_b": ((0.0, 9.0), (0.0, 0.0)),
            "v_a": 5.0,
            "v_b": 5.0,
            "t0": t0,
            "t1": t1,
        },
        {
            "label": "No overlap: meeting ruled out",
            "fixes_a": ((0.0, 0.0), (5.0, 0.0)),
            "fixes_b": ((0.0, 8.0), (5.0, 8.0)),
            "v_a": 4.0,
            "v_b": 4.0,
            "t0": t0,
            "t1": t1,
        },
    ]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for ax, scenario in zip(axes, scenarios):
        plot_scenario(ax, scenario)

        e_a = reachable_ellipse(
            scenario["fixes_a"][0], scenario["fixes_a"][1], scenario["v_a"], t1 - t0
        )
        e_b = reachable_ellipse(
            scenario["fixes_b"][0], scenario["fixes_b"][1], scenario["v_b"], t1 - t0
        )
        overlap = e_a.intersection(e_b)
        simultaneous = simultaneous_points(
            overlap,
            scenario["fixes_a"],
            scenario["fixes_b"],
            scenario["v_a"],
            scenario["v_b"],
            t0,
            t1,
        )

        print(f"\n{scenario['label']}")
        print(f"  Moose A ellipse area: {e_a.area:9.3f} km^2")
        print(f"  Moose B ellipse area: {e_b.area:9.3f} km^2")
        print(f"  Overlap area:         {overlap.area:9.3f} km^2")

        if overlap.is_empty:
            print("  Verdict: no shared place, so no meeting under this v_max")
        elif not simultaneous:
            print("  Verdict: shared places exist, but never at a shared time")
        else:
            best = max(simultaneous, key=lambda row: row[3] - row[2])
            x, y, lo, hi = best
            print(f"  Candidate meeting places on grid: {len(simultaneous)}")
            print(
                f"  Widest window at ({x:.2f}, {y:.2f}) km: t in [{lo:.3f}, {hi:.3f}] h"
            )

    fig.suptitle(
        "Reachable ellipses for two moose over t in [0, 2] h under three assumptions"
    )
    fig.tight_layout()

    output_file = "figures/cooccurrence_feasibility.png"
    fig.savefig(output_file, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"\nSaved plot to: {output_file}")


if __name__ == "__main__":
    main()
