# moose-ellipse

Reachable-ellipse geometry for locating a moose between two GPS fixes.

A GPS collar gives a sequence of positions and times but says nothing about the
path between them. If a moose can travel no faster than some maximum speed
`v_max`, the set of places it could have occupied between two consecutive fixes
is an ellipse whose foci are the two fixes. Intersecting the ellipses of two
animals is a cheap first test of whether they could have met, and adding a time
window turns "could they have shared a place" into "could they have shared a
place *at the same time*".

This package is the code from the blog post
[Ellipse Intersections and Locating a Moose Between Fixes](https://galenseilis.github.io/blog/posts/ellipse-intersections-for-moose-movement/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ellipse-intersections-for-moose-movement"
```

Requires Python 3.11 or newer, and depends on `shapely`, `numpy`, and
`matplotlib`.

## Quick start

```python
from moose_ellipse import reachable_ellipse
from shapely.geometry import Point

# A moose fixed at (0, 0) and later at (5, 1) km, with two hours to get there
# at no more than 6 km/h.
region = reachable_ellipse((0.0, 0.0), (5.0, 1.0), v_max=6.0, dt=2.0)
region.area  # potential path area in km^2
region.contains(Point(2.5, 0.5))
```

Build the figures shown in the post with the two console scripts:

```bash
moose-ellipse-shared-focus   # figures/ellipse_intersection.png
moose-ellipse-reach          # figures/cooccurrence_feasibility.png
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
