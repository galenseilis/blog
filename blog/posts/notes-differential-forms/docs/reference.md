# API reference

## `notes_differential_forms.tangent_space_cubic.plot_tangent_space_cubic(output="figures/tangent_space_cubic.png")`

Draw the tangent space to `y = x**3 - 10x` at `(2, -12)`. `output` may be a
`str` or `pathlib.Path`; parent directories are created. Returns the written
`pathlib.Path`.

## `notes_differential_forms.tangent_space_quadratic.plot_tangent_space_quadratic(output="figures/tangent_space_quadratic.png")`

Draw the tangent space to `y = x**2` at `(1, 1)`. Returns the written
`pathlib.Path`.

## `notes_differential_forms.tangent_space_axes.plot_tangent_space_axes(output="figures/tangent_space_axes.png")`

Draw a tangent vector `<c, d>` against the differential axes `dx` and `dy`.
Returns the written `pathlib.Path`.

## `notes_differential_forms.figures.render_all(output_dir="figures")`

Render all three figures into `output_dir` and return the list of written
paths, in the order the post presents them.

## `notes_differential_forms.figures.main()`

Console-script entry point. Calls `render_all()` and prints each written path.

## Console scripts

| Command | Writes |
| --- | --- |
| `notes-differential-forms` | `figures/tangent_space_cubic.png`, `figures/tangent_space_quadratic.png`, `figures/tangent_space_axes.png` |
