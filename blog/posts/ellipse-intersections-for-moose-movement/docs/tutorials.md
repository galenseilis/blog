# Tutorial

This tutorial builds a reachable ellipse for one animal and then runs a
two-animal co-occurrence test. It should take a few minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ellipse-intersections-for-moose-movement"
```

## 2. A reachable ellipse for one interval

Suppose a moose is fixed at `(0, 0)` km at `t = 0` and at `(5, 1)` km at
`t = 2` h, and that it cannot exceed `6` km/h.

```python
from moose_ellipse import reachable_ellipse

region = reachable_ellipse((0.0, 0.0), (5.0, 1.0), v_max=6.0, dt=2.0)
print(region.area)
```

The result is a Shapely geometry. Its foci are the two fixes, so both fixes lie
on its boundary. Everything inside is a position the animal could have occupied
at *some* moment during the interval.

## 3. Ask about a specific place

`presence_window` returns the range of times at which an animal could have been
at a particular point.

```python
from moose_ellipse.reach import presence_window

lo, hi = presence_window((2.5, 0.5), (0.0, 0.0), (5.0, 1.0), v_max=6.0, t0=0.0, t1=2.0)
print(lo, hi)
```

If `lo <= hi` there is a feasible time; otherwise the point cannot be reached
in time.

## 4. Could two animals have met?

Give two animals each a pair of fixes and a speed, and grid the overlap of
their reachable ellipses for points where their presence windows overlap.

```python
from moose_ellipse.reach import Scenario, summarise

scenario = Scenario(
    label="example",
    fixes_a=((0.0, 0.0), (5.0, 1.0)),
    fixes_b=((6.0, 0.0), (1.0, 2.0)),
    v_a=6.0,
    v_b=6.0,
    t0=0.0,
    t1=2.0,
)
print(summarise(scenario)["verdict"])
```

`summarise` reports the areas, the number of candidate meeting places on the
grid, and the verdict: a feasible meeting, a spatial overlap that never
coincides in time, or no overlap at all.

## 5. Reproduce the post's figures

```bash
moose-ellipse-shared-focus   # writes figures/ellipse_intersection.png
moose-ellipse-reach          # writes figures/cooccurrence_feasibility.png
```

You now know the whole workflow: build ellipses, intersect them, and refine the
question with the time axis. Next, read the [how-to guides](how-to-guides.md)
for practical recipes.
