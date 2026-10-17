# API reference

## Geometry primitives

### `moose_ellipse.geometry.ellipse(cx, cy, a, b, angle_deg, resolution=256)`

Return a Shapely ellipse centred at `(cx, cy)` with semi-axes `a >= b`,
rotated `angle_deg` degrees counter-clockwise.

### `moose_ellipse.geometry.ellipse_foci(cx, cy, a, b, angle_deg)`

Return the two foci of an oriented ellipse as a list of `(x, y)` pairs.

Raises `ValueError` if `a < b`.

### `moose_ellipse.geometry.polygons(geometry)`

Return the polygonal parts of a Shapely geometry as a list, normalising empty
and multi-part results.

### `moose_ellipse.geometry.plot_geometry(geometry, ax, **kwargs)`

Fill every polygonal part of `geometry` on the Matplotlib axes `ax`.

### `moose_ellipse.geometry.plot_boundary(geometry, ax, **kwargs)`

Draw the boundary of every polygonal part of `geometry` on `ax`.

## Reachability

### `moose_ellipse.reach.reachable_ellipse(fix0, fix1, v_max, dt)`

Return the potential path area between two fixes. `fix0` and `fix1` are
`(x, y)` kilometres, `v_max` is km/h, and `dt` is hours.

Raises `ValueError` when `2 * v_max * dt < |fix1 - fix0|`.

### `moose_ellipse.reach.presence_window(p, fix0, fix1, v_max, t0, t1)`

Return the `(lo, hi)` times in `[t0, t1]` at which an animal could be at point
`p`.

### `moose_ellipse.reach.simultaneous_points(region, fixes_a, fixes_b, v_max_a, v_max_b, t0, t1, step=0.05)`

Grid `region` for points where both animals' presence windows overlap. Returns
a list of `(x, y, lo, hi)` rows.

### `moose_ellipse.reach.Scenario`

A frozen dataclass describing a two-animal comparison: `label`, `fixes_a`,
`fixes_b`, `v_a`, `v_b`, `t0`, `t1`.

### `moose_ellipse.reach.default_scenarios()`

Return the three illustrative scenarios used in the blog post.

### `moose_ellipse.reach.summarise(scenario)`

Return a dict with `area_a`, `area_b`, `overlap_area`, `n_meeting_places`, and
`verdict` (plus `best_x`, `best_y`, `best_lo`, `best_hi` when a meeting is
feasible).

### `moose_ellipse.reach.plot_scenario(ax, scenario)`

Draw one scenario's reachable ellipses and feasible meeting places on `ax`.

### `moose_ellipse.reach.run(output="figures/cooccurrence_feasibility.png")`

Render the three-scenario figure and return the written `Path`.

## Shared focus

### `moose_ellipse.shared_focus.EllipseSpec`

A frozen dataclass with `cx`, `cy`, `a`, `b`, `angle_deg`.

### `moose_ellipse.shared_focus.build_shared_focus_demo(e1=EllipseSpec(0, 0, 5, 3, 20), e2_a=4, e2_b=2, e2_angle=-35)`

Construct a `SharedFocusDemo`: two oriented ellipses that share a focus, along
with their intersection and exclusive areas.

### `moose_ellipse.shared_focus.plot_shared_focus(demo, ax)`

Draw the shared-focus demo on `ax`.

### `moose_ellipse.shared_focus.run(output="figures/ellipse_intersection.png")`

Render the shared-focus figure and return the written `Path`.

## Console scripts

| Command | Writes |
| --- | --- |
| `moose-ellipse-shared-focus` | `figures/ellipse_intersection.png` |
| `moose-ellipse-reach` | `figures/cooccurrence_feasibility.png` |
