# Explanation

## Why the reachable region is an ellipse

A moose observed at $x_0$ at time $t_0$ and at $x_1$ at time $t_1$ can be at a
point $p$ at some moment during the interval only if there is a route from
$x_0$ through $p$ to $x_1$ that fits within the available time. The shortest
such route is the two straight segments $x_0 \to p$ and $p \to x_1$, so with a
maximum speed $v_{\max}$ the condition is

$$\lVert p - x_0 \rVert + \lVert p - x_1 \rVert \le v_{\max}\,\Delta t.$$

A set of points whose distances to two fixed points sum to a constant is, by
definition, an ellipse with those two points as foci. So the reachable region of
a single time step is a filled ellipse, the **potential path area** from time
geography. Its semi-major axis is $a = v_{\max}\Delta t / 2$, the centre is the
midpoint of the fixes, and the major axis lies along the segment joining them.

The ellipse grows linearly in its long direction with $\Delta t$, so the method
loses power exactly when fixes are sparse.

## A region, not a path, and not a probability

The ellipse is the union, over every moment in the interval, of the positions
the animal could have occupied. It is much larger than any real trajectory, and
it says nothing about likelihood. It answers "could" rather than "did" or
"probably".

## Space and time

Because the ellipse is time-agnostic, two animals can have overlapping ellipses
while occupying the same place at disjoint times. To sharpen the test, note that
an animal that must be at $x_0$ at $t_0$ and at $x_1$ at $t_1$ can be at $p$ at
time $t$ only if

$$t_0 + \frac{\lVert p - x_0 \rVert}{v_{\max}} \le t \le t_1 - \frac{\lVert p - x_1 \rVert}{v_{\max}}.$$

Two animals could have met at $p$ only if these windows overlap. A meeting is
possible if such a $p$ exists anywhere in the intersection of the two ellipses.
`simultaneous_points` searches for these points on a grid.

## Strengths

- **Cheap and closed-form.** Two fixes, one speed, and a formula.
- **Interpretable.** Every component has a physical meaning, and the speed
  assumption can be argued with directly.
- **Sound for ruling things out.** A non-intersection is a genuine
  assumption-conditional impossibility result, which makes a good screen before
  committing to expensive movement models.
- **Composable.** Ellipses chain across intervals into a potential path area for
  a whole tracking period.

## Limitations

The maximum speed is the most consequential assumption and it cuts both ways:
too high and the test almost never rules anything out, too low and feasible
meetings are falsely excluded. Real speeds depend on terrain, snow, season,
sex, presence of a calf, and behaviour, so the honest approach is to report
results across a range of plausible speeds.

Beyond the speed assumption:

- **Barriers and habitat.** Straight-line reachability ignores lakes, rivers,
  cliffs, highways, and fences. Least-cost distances fix this but the reachable
  region is generally no longer an ellipse.
- **Location error.** Fixes are uncertain, so the true region is the ellipse
  dilated by the error radius, and error can make the implied speed exceed
  $v_{\max}$.
- **Geometry versus probability.** The method makes no statement about
  likelihood, and co-location is not the same as interaction.
- **Temporal resolution.** Whether an interaction is detectable depends on the
  sampling interval relative to encounter duration.
- **Independence.** With two tracked animals, both movement and error are
  treated as independent, which can fail when they share a clock or respond to
  the same weather.
- **Planar approximation.** Distances must be computed in a local projected
  frame, not in raw degrees.
