# How-to guides

Practical recipes for common tasks.

## Reproduce the figures from the blog post

Run the console script from the post directory:

```bash
chatgpt-plot-covering-diagram
```

It writes `figures/chatgpt_cover_relation_plotter_output.png`. The second,
failing example is available from Python:

```python
from chatgpt_plot_covering_diagram.failing_example import failing_example

failing_example("figures/chatgpt_cover_relation_plotter_output_test.png")
```

## Draw into an existing axes

Pass the `ax` you want the graph drawn on; the function returns it so calls
chain:

```python
import matplotlib.pyplot as plt
import networkx as nx

from chatgpt_plot_covering_diagram import covering_diagram

dg = nx.DiGraph([("a", "b"), ("b", "c")])
fig, ax = plt.subplots(figsize=(5, 5))
covering_diagram(dg, ax=ax).set_title("My order")
fig.savefig("my_order.png")
```

## Save with a transparent background

The post's figures use transparent backgrounds, which is why the examples
pass `transparent=True` to `savefig`:

```python
ax = covering_diagram(dg)
ax.figure.savefig("covering.png", dpi=300, transparent=True)
```

## Run the examples with custom output paths

Both example functions take an output path and create its parent directory:

```python
from chatgpt_plot_covering_diagram.full_example import full_example

full_example("out/full.png")
full_example("out/nested/deeper/full.png")
```

## Adjust the figure size

When you do not supply an axes the function builds an `8 x 8` inch figure.
Supply your own to change the size:

```python
fig, ax = plt.subplots(figsize=(4, 10))
covering_diagram(dg, ax=ax)
```
