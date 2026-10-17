# Tutorial

This tutorial draws a covering-style diagram from a `networkx.DiGraph` and
then reproduces the two examples from the blog post. It should take a couple
of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/chatgpt-plot-covering-diagram"
```

## 2. Draw a diagram

Build a small partial order as a directed graph and pass it to
`covering_diagram`:

```python
import networkx as nx

from chatgpt_plot_covering_diagram import covering_diagram

dg = nx.DiGraph()
dg.add_edges_from([("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")])

ax = covering_diagram(dg)
ax.figure.savefig("example.png", dpi=300, transparent=True)
```

The function creates its own figure when you do not pass an `ax`, and returns
the axes so that you can save, title, or embed it.

## 3. Reuse your own axes

Because `covering_diagram` accepts an axis, it composes with any other
Matplotlib figure:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
covering_diagram(dg, ax=axes[0])
covering_diagram(dg, ax=axes[1])
fig.savefig("two-panels.png")
```

## 4. Reproduce the post's examples

The two graphs the post uses have named helpers:

```python
from chatgpt_plot_covering_diagram.full_example import full_example
from chatgpt_plot_covering_diagram.failing_example import failing_example

full_example("figures/chatgpt_cover_relation_plotter_output.png")
failing_example("figures/chatgpt_cover_relation_plotter_output_test.png")
```

`full_example` draws the six-node order from the post, and `failing_example`
draws the smaller order that the author uses to show the function's output
does not match the expected covering diagram.

You now know the whole surface of the package. Next, read the
[how-to guides](how-to-guides.md) for saving and embedding recipes.
