# Tutorial

This tutorial renders the tangent-space figures from the post and explains
what each one shows. It should take a couple of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-differential-forms"
```

## 2. The tangent space to a cubic

The first figure puts a curve and its tangent space in the same plane:

```python
from notes_differential_forms import plot_tangent_space_cubic

plot_tangent_space_cubic("figures/tangent_space_cubic.png")
```

The yellow curve is `y = x**3 - 10x`. The magenta line is the tangent space
`T_pC`, which is spanned by the tangent vector `(1, f'(a))` drawn in blue.
The dashed magenta lines are the pullbacks of the point `p = (a, f(a))` onto
each axis.

## 3. The tangent space to a parabola

The second figure repeats the construction for `y = x**2` at `(1, 1)`:

```python
from notes_differential_forms import plot_tangent_space_quadratic

plot_tangent_space_quadratic("figures/tangent_space_quadratic.png")
```

Reading the tangent vector as `(dx, dy) = (1, 2a)` gives `dy/dx = 2a`, the
familiar derivative recovered from the differential coordinates.

## 4. The differential axes

The third figure draws a tangent vector against the differential axes:

```python
from notes_differential_forms import plot_tangent_space_axes

plot_tangent_space_axes("figures/tangent_space_axes.png")
```

`dx` and `dy` are drawn as a separate pair of axes, and the vector `<c, d>`
is placed on them; `a` and `b` mark the ambient coordinates of the point.

## 5. Render everything at once

```python
from notes_differential_forms.figures import render_all

render_all("figures")
```

or run `notes-differential-forms` from the post directory. You now have every
figure the post embeds. Next, read the [how-to guides](how-to-guides.md) for
customising them.
