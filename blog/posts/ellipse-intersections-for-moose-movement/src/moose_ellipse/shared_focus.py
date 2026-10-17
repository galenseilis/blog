"""Two arbitrarily oriented ellipses that share a focus.

This is the worked example from the first half of the blog post: build one
ellipse, take one of its foci, construct a second ellipse rotated to a
different angle that passes through that same focus, and then fill the
set-theoretic regions (each ellipse only, and the overlap).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from shapely.geometry.base import BaseGeometry

from moose_ellipse.geometry import ellipse, ellipse_foci, plot_geometry


@dataclass(frozen=True)
class EllipseSpec:
    """The parameters that define one ellipse."""

    cx: float
    cy: float
    a: float
    b: float
    angle_deg: float


@dataclass(frozen=True)
class SharedFocusDemo:
    """The geometry produced by the shared-focus construction."""

    e1: BaseGeometry
    e2: BaseGeometry
    e1_spec: EllipseSpec
    e2_spec: EllipseSpec
    foci1: list[tuple[float, float]]
    foci2: list[tuple[float, float]]
    shared_focus: tuple[float, float]
    intersection: BaseGeometry
    e1_only: BaseGeometry
    e2_only: BaseGeometry


def build_shared_focus_demo(
    e1: EllipseSpec = EllipseSpec(0, 0, 5, 3, 20),
    e2_a: float = 4,
    e2_b: float = 2,
    e2_angle: float = -35,
) -> SharedFocusDemo:
    """Construct a pair of ellipses that share one focus.

    The first ellipse is placed at the origin. The second is translated so
    that its leading focus lands exactly on the first focus of the first
    ellipse, then the two are intersected.

    Parameters
    ----------
    e1:
        Parameters of the first ellipse.
    e2_a, e2_b:
        Semi-major and semi-minor axes of the second ellipse.
    e2_angle:
        Rotation of the second ellipse's major axis, in degrees.
    """
    first = ellipse(e1.cx, e1.cy, e1.a, e1.b, e1.angle_deg)
    foci1 = ellipse_foci(e1.cx, e1.cy, e1.a, e1.b, e1.angle_deg)

    shared_focus = foci1[0]

    # For an ellipse, c = sqrt(a^2 - b^2) is the centre-to-focus distance.
    # The shared focus sits at centre - c * direction, so the second centre
    # is shared_focus + c * direction along its major axis.
    c2 = math.sqrt(e2_a**2 - e2_b**2)
    theta2 = math.radians(e2_angle)
    direction2 = (math.cos(theta2), math.sin(theta2))

    e2_spec = EllipseSpec(
        cx=shared_focus[0] + c2 * direction2[0],
        cy=shared_focus[1] + c2 * direction2[1],
        a=e2_a,
        b=e2_b,
        angle_deg=e2_angle,
    )

    second = ellipse(e2_spec.cx, e2_spec.cy, e2_spec.a, e2_spec.b, e2_spec.angle_deg)
    foci2 = ellipse_foci(e2_spec.cx, e2_spec.cy, e2_spec.a, e2_spec.b, e2_spec.angle_deg)

    return SharedFocusDemo(
        e1=first,
        e2=second,
        e1_spec=e1,
        e2_spec=e2_spec,
        foci1=foci1,
        foci2=foci2,
        shared_focus=shared_focus,
        intersection=first.intersection(second),
        e1_only=first.difference(second),
        e2_only=second.difference(first),
    )


def _label_region(geometry: BaseGeometry, text: str, ax: Axes, **kwargs: object) -> None:
    if not geometry.is_empty:
        point = geometry.representative_point()
        ax.annotate(text, (point.x, point.y), ha="center", va="center", **kwargs)


def plot_shared_focus(demo: SharedFocusDemo, ax: Axes) -> None:
    """Draw the shared-focus demo on ``ax``."""
    e1_spec, e2_spec = demo.e1_spec, demo.e2_spec

    plot_geometry(demo.e1_only, ax, color="cornflowerblue", alpha=0.65)
    plot_geometry(demo.e2_only, ax, color="salmon", alpha=0.65)
    plot_geometry(demo.intersection, ax, color="mediumseagreen", alpha=0.85)

    for geometry, color, label in [
        (demo.e1, "blue", "Ellipse 1"),
        (demo.e2, "red", "Ellipse 2"),
    ]:
        x, y = geometry.exterior.xy
        ax.plot(x, y, color=color, linewidth=2, label=label)

    ax.scatter(
        e1_spec.cx, e1_spec.cy, color="blue", marker="+", s=100, linewidths=2, zorder=10
    )
    ax.scatter(
        e2_spec.cx, e2_spec.cy, color="red", marker="+", s=100, linewidths=2, zorder=10
    )

    for i, (x, y) in enumerate(demo.foci1, 1):
        ax.scatter(x, y, color="blue", marker="x", s=90, linewidths=2.5, zorder=11)
        if (x, y) != demo.shared_focus:
            ax.annotate(
                f"F{i} (E1)",
                (x, y),
                xytext=(8, 8),
                textcoords="offset points",
                color="darkblue",
                fontsize=10,
                fontweight="bold",
            )

    for i, (x, y) in enumerate(demo.foci2, 1):
        is_shared = math.isclose(x, demo.shared_focus[0], abs_tol=1e-9) and math.isclose(
            y, demo.shared_focus[1], abs_tol=1e-9
        )
        if is_shared:
            ax.scatter(
                x,
                y,
                color="purple",
                marker="*",
                s=180,
                edgecolor="black",
                linewidth=0.8,
                zorder=12,
                label="Shared focus",
            )
            ax.annotate(
                "Shared focus\n(E1 & E2)",
                (x, y),
                xytext=(10, -35),
                textcoords="offset points",
                color="purple",
                fontsize=10,
                fontweight="bold",
                ha="left",
            )
        else:
            ax.scatter(x, y, color="red", marker="x", s=90, linewidths=2.5, zorder=11)
            ax.annotate(
                f"F{i} (E2)",
                (x, y),
                xytext=(8, 8),
                textcoords="offset points",
                color="darkred",
                fontsize=10,
                fontweight="bold",
            )

    _label_region(
        demo.e1_only,
        f"Ellipse 1 only\n{demo.e1_only.area:.3f}",
        ax,
        fontsize=11,
        color="darkblue",
    )
    _label_region(
        demo.e2_only,
        f"Ellipse 2 only\n{demo.e2_only.area:.3f}",
        ax,
        fontsize=11,
        color="darkred",
    )
    _label_region(
        demo.intersection,
        f"Overlap\n{demo.intersection.area:.3f}",
        ax,
        fontsize=11,
        color="darkgreen",
        fontweight="bold",
    )

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Overlap of Two Arbitrarily Oriented Ellipses\nwith a Shared Focus")
    ax.legend()
    ax.grid(True, alpha=0.25)


def run(output: str | Path = "figures/ellipse_intersection.png") -> Path:
    """Render the shared-focus figure and return the written path."""
    demo = build_shared_focus_demo()

    print("Ellipse 1 foci:")
    for i, (x, y) in enumerate(demo.foci1, 1):
        print(f"  F{i}: ({x:.6f}, {y:.6f})")

    print("\nEllipse 2 foci:")
    for i, (x, y) in enumerate(demo.foci2, 1):
        print(f"  F{i}: ({x:.6f}, {y:.6f})")

    print(f"\nShared focus: ({demo.shared_focus[0]:.6f}, {demo.shared_focus[1]:.6f})")

    print(f"\nEllipse 1 area:       {demo.e1.area:.6f}")
    print(f"Ellipse 2 area:       {demo.e2.area:.6f}")
    print(f"Intersection area:    {demo.intersection.area:.6f}")
    print(f"Ellipse 1 only area:  {demo.e1_only.area:.6f}")
    print(f"Ellipse 2 only area:  {demo.e2_only.area:.6f}")

    fig, ax = plt.subplots(figsize=(10, 7))
    plot_shared_focus(demo, ax)
    plt.tight_layout()

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=600, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    print(f"\nSaved plot to: {output_path}")
    return output_path


def main() -> None:
    """Console-script entry point."""
    run()


if __name__ == "__main__":
    main()
