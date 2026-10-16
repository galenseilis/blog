import math
import matplotlib.pyplot as plt

from shapely.geometry import Point
from shapely.affinity import scale, rotate, translate


def ellipse(cx, cy, a, b, angle_deg, resolution=256):
    e = Point(0, 0).buffer(1, quad_segs=resolution)
    e = scale(e, a, b)
    e = rotate(e, angle_deg, origin=(0, 0))
    e = translate(e, cx, cy)
    return e


def ellipse_foci(cx, cy, a, b, angle_deg):
    """
    Return the two foci of an ellipse.

    The ellipse has:
        center = (cx, cy)
        semi-major axis = a
        semi-minor axis = b
        rotation = angle_deg
    """
    if a < b:
        raise ValueError("This function expects a >= b.")

    c = math.sqrt(a**2 - b**2)

    theta = math.radians(angle_deg)

    dx = c * math.cos(theta)
    dy = c * math.sin(theta)

    return [
        (cx - dx, cy - dy),
        (cx + dx, cy + dy),
    ]


# ------------------------------------------------------------------
# Define ellipses
# ------------------------------------------------------------------

# Ellipse 1
e1_cx = 0
e1_cy = 0
e1_a = 5
e1_b = 3
e1_angle = 20

e1 = ellipse(
    e1_cx,
    e1_cy,
    e1_a,
    e1_b,
    e1_angle,
)


# Get Ellipse 1 foci
foci1 = ellipse_foci(
    e1_cx,
    e1_cy,
    e1_a,
    e1_b,
    e1_angle,
)

# Use the first focus of Ellipse 1 as a focus of Ellipse 2.
shared_focus = foci1[0]


# ------------------------------------------------------------------
# Define Ellipse 2 so that it shares a focus with Ellipse 1
# ------------------------------------------------------------------

e2_a = 4
e2_b = 2
e2_angle = -35

# For an ellipse:
#
#     c = sqrt(a^2 - b^2)
#
# and the distance from the center to either focus is c.
#
# The shared focus is:
#
#     center - c * direction
#
# Therefore:
#
#     center = shared_focus + c * direction
#
# where "direction" is the direction of the major axis.

e2_c = math.sqrt(e2_a**2 - e2_b**2)

theta2 = math.radians(e2_angle)

direction2 = (
    math.cos(theta2),
    math.sin(theta2),
)

e2_cx = shared_focus[0] + e2_c * direction2[0]
e2_cy = shared_focus[1] + e2_c * direction2[1]

e2 = ellipse(
    e2_cx,
    e2_cy,
    e2_a,
    e2_b,
    e2_angle,
)


# Get Ellipse 2 foci
foci2 = ellipse_foci(
    e2_cx,
    e2_cy,
    e2_a,
    e2_b,
    e2_angle,
)


# ------------------------------------------------------------------
# Print focus information
# ------------------------------------------------------------------

print("Ellipse 1 foci:")
for i, (x, y) in enumerate(foci1, 1):
    print(f"  F{i}: ({x:.6f}, {y:.6f})")

print("\nEllipse 2 foci:")
for i, (x, y) in enumerate(foci2, 1):
    print(f"  F{i}: ({x:.6f}, {y:.6f})")

print(f"\nShared focus: ({shared_focus[0]:.6f}, {shared_focus[1]:.6f})")


# ------------------------------------------------------------------
# Compute regions
# ------------------------------------------------------------------

intersection = e1.intersection(e2)
e1_only = e1.difference(e2)
e2_only = e2.difference(e1)


# Areas
area_e1 = e1.area
area_e2 = e2.area
area_intersection = intersection.area
area_e1_only = e1_only.area
area_e2_only = e2_only.area


print(f"\nEllipse 1 area:       {area_e1:.6f}")
print(f"Ellipse 2 area:       {area_e2:.6f}")
print(f"Intersection area:    {area_intersection:.6f}")
print(f"Ellipse 1 only area:  {area_e1_only:.6f}")
print(f"Ellipse 2 only area:  {area_e2_only:.6f}")


# ------------------------------------------------------------------
# Plot
# ------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 7))


def plot_geometry(geometry, ax, **kwargs):
    if geometry.is_empty:
        return

    if geometry.geom_type == "Polygon":
        polygons = [geometry]
    else:
        polygons = list(geometry.geoms)

    for polygon in polygons:
        x, y = polygon.exterior.xy
        ax.fill(x, y, **kwargs)


# ------------------------------------------------------------------
# Fill regions
# ------------------------------------------------------------------

plot_geometry(
    e1_only,
    ax,
    color="cornflowerblue",
    alpha=0.65,
)

plot_geometry(
    e2_only,
    ax,
    color="salmon",
    alpha=0.65,
)

plot_geometry(
    intersection,
    ax,
    color="mediumseagreen",
    alpha=0.85,
)


# ------------------------------------------------------------------
# Draw ellipse boundaries
# ------------------------------------------------------------------

for geometry, color, label in [
    (e1, "blue", "Ellipse 1"),
    (e2, "red", "Ellipse 2"),
]:
    x, y = geometry.exterior.xy
    ax.plot(
        x,
        y,
        color=color,
        linewidth=2,
        label=label,
    )


# ------------------------------------------------------------------
# Draw centers
# ------------------------------------------------------------------

ax.scatter(
    e1_cx,
    e1_cy,
    color="blue",
    marker="+",
    s=100,
    linewidths=2,
    zorder=10,
)

ax.scatter(
    e2_cx,
    e2_cy,
    color="red",
    marker="+",
    s=100,
    linewidths=2,
    zorder=10,
)


# ------------------------------------------------------------------
# Draw foci
# ------------------------------------------------------------------

# Ellipse 1 foci
for i, (x, y) in enumerate(foci1, 1):
    ax.scatter(
        x,
        y,
        color="blue",
        marker="x",
        s=90,
        linewidths=2.5,
        zorder=11,
    )

    # Don't duplicate the label for the shared focus.
    if (x, y) != shared_focus:
        ax.annotate(
            f"F{i} (E1)",
            (x, y),
            xytext=(8, 8),
            textcoords="offset points",
            color="darkblue",
            fontsize=10,
            fontweight="bold",
        )


# Ellipse 2 foci
for i, (x, y) in enumerate(foci2, 1):
    # Shared focus gets a special marker.
    if math.isclose(x, shared_focus[0], abs_tol=1e-9) and math.isclose(
        y, shared_focus[1], abs_tol=1e-9
    ):
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
        ax.scatter(
            x,
            y,
            color="red",
            marker="x",
            s=90,
            linewidths=2.5,
            zorder=11,
        )

        ax.annotate(
            f"F{i} (E2)",
            (x, y),
            xytext=(8, 8),
            textcoords="offset points",
            color="darkred",
            fontsize=10,
            fontweight="bold",
        )


# ------------------------------------------------------------------
# Label regions
# ------------------------------------------------------------------


def label_region(geometry, text, ax, **kwargs):
    if not geometry.is_empty:
        point = geometry.representative_point()
        ax.annotate(
            text,
            (point.x, point.y),
            ha="center",
            va="center",
            **kwargs,
        )


label_region(
    e1_only,
    f"Ellipse 1 only\n{area_e1_only:.3f}",
    ax,
    fontsize=11,
    color="darkblue",
)

label_region(
    e2_only,
    f"Ellipse 2 only\n{area_e2_only:.3f}",
    ax,
    fontsize=11,
    color="darkred",
)

label_region(
    intersection,
    f"Overlap\n{area_intersection:.3f}",
    ax,
    fontsize=11,
    color="darkgreen",
    fontweight="bold",
)


# ------------------------------------------------------------------
# Formatting
# ------------------------------------------------------------------

ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Overlap of Two Arbitrarily Oriented Ellipses\nwith a Shared Focus")

ax.legend()
ax.grid(True, alpha=0.25)

plt.tight_layout()


# ------------------------------------------------------------------
# Save instead of displaying
# ------------------------------------------------------------------

output_file = "ellipse_intersection.png"

fig.savefig(
    output_file,
    dpi=600,
    bbox_inches="tight",
    facecolor="white",
)

plt.close(fig)

print(f"\nSaved plot to: {output_file}")
