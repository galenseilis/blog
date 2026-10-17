# API reference

## `parity_decomposition_in_python.parity`

### `even_part(f, t)`

Compute even part: (f(t) + f(-t))/2.

### `odd_part(f, t)`

Compute odd part: (f(t) - f(-t))/2.

### `parity_decomposition_vector(f, t)`

Return (even_part(t), odd_part(t)).

### `plot_parity_decomposition(f, t, output="example_parity_decomposition.png", dpi=300, transparent=True)`

Plot and save parity decomposition.

### `example_f(t)`

Example function from the blog post.

### `main()`

Generate the example plot.
