# How-to guides

Practical recipes for common tasks.

## Reproduce the post's figures

From the post directory:

```bash
notes-differential-forms
```

This writes `figures/tangent_space_cubic.png`,
`figures/tangent_space_quadratic.png`, and `figures/tangent_space_axes.png`.

## Write a single figure to a custom path

Each plot function takes an output path and creates its parent directory:

```python
from notes_differential_forms import plot_tangent_space_quadratic

plot_tangent_space_quadratic("out/tangent.png")
```

## Render a different set of figures

Call only the functions you need:

```python
from notes_differential_forms import (
    plot_tangent_space_axes,
    plot_tangent_space_cubic,
)

plot_tangent_space_cubic("out/cubic.png")
plot_tangent_space_axes("out/axes.png")
```

## Change the output directory

`render_all` accepts any directory:

```python
from pathlib import Path

from notes_differential_forms.figures import render_all

paths = render_all(Path("build") / "figures")
print([str(path) for path in paths])
```

## Embed a figure in your own Matplotlib figure

The plotting functions build and close their own figures. To reuse the drawing
in a larger figure, copy the body of the function you need, or save the PNG
and include it in your document.
