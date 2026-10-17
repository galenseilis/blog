# How-to guides

Practical recipes for common tasks.

## Reproduce the figures from the blog post

Run the two console scripts from the post directory:

```bash
moose-ellipse-shared-focus
moose-ellipse-reach
```

Each writes a PNG into `figures/`. Pass a different path to control the output:

```python
from moose_ellipse.shared_focus import run as run_shared_focus
from moose_ellipse.reach import run as run_reach

run_shared_focus("out/shared_focus.png")
run_reach("out/cooccurrence.png")
```

## Handle fixes that look impossible

`reachable_ellipse` raises `ValueError` when the two fixes are farther apart
than the animal could travel in the interval at the given speed. This is often
a sign that the speed bound is too low or that the fixes carry location error.

```python
from moose_ellipse import reachable_ellipse

try:
    reachable_ellipse((0.0, 0.0), (100.0, 0.0), v_max=1.0, dt=1.0)
except ValueError as exc:
    print("infeasible:", exc)
```

To explore sensitivity, loop over a range of plausible speeds and report where
the verdict flips.

```python
from moose_ellipse.reach import Scenario, summarise

for v in (2.0, 4.0, 6.0, 8.0):
    scenario = Scenario(
        label=f"v={v}",
        fixes_a=((0.0, 0.0), (9.0, 0.0)),
        fixes_b=((0.0, 9.0), (0.0, 0.0)),
        v_a=v,
        v_b=v,
        t0=0.0,
        t1=2.0,
    )
    print(v, summarise(scenario)["verdict"])
```

## Change the grid resolution of the meeting search

`simultaneous_points` samples the overlap on a grid of spacing `step`
(default `0.05` km). Smaller steps give a finer search at more cost.

```python
from moose_ellipse import reachable_ellipse
from moose_ellipse.reach import simultaneous_points

e_a = reachable_ellipse((0.0, 0.0), (5.0, 1.0), 6.0, 2.0)
e_b = reachable_ellipse((6.0, 0.0), (1.0, 2.0), 6.0, 2.0)
overlap = e_a.intersection(e_b)
points = simultaneous_points(
    overlap,
    ((0.0, 0.0), (5.0, 1.0)),
    ((6.0, 0.0), (1.0, 2.0)),
    6.0,
    6.0,
    0.0,
    2.0,
    step=0.01,
)
print(len(points))
```

## Work in a local projected frame

Coordinates must be projected to a local metric frame (metres or kilometres)
before use. Raw longitude/latitude degrees distort distances. Reproject fixes
first and keep a single unit system throughout.

## Build your own scenario figure

```python
import matplotlib.pyplot as plt

from moose_ellipse.reach import Scenario, plot_scenario

scenario = Scenario(
    label="custom",
    fixes_a=((0.0, 0.0), (5.0, 1.0)),
    fixes_b=((6.0, 0.0), (1.0, 2.0)),
    v_a=6.0,
    v_b=6.0,
    t0=0.0,
    t1=2.0,
)
fig, ax = plt.subplots(figsize=(6, 5))
plot_scenario(ax, scenario)
fig.savefig("custom.png", dpi=300, bbox_inches="tight", facecolor="white")
```
