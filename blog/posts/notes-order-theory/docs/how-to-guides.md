# How-to guides

Practical recipes for common tasks.

## Reproduce the post's figures

From the post directory:

```bash
notes-order-theory
```

This writes `figures/example_partial_order.png` and
`figures/cover_diagram.png`.

## Draw a different partial order

`build_digraph` accepts any list of two-character pairs:

```python
from notes_order_theory import build_digraph

graph = build_digraph(["ab", "bc", "ac"])
```

Then draw it with your own layout using `networkx`.

## Change the cover-diagram layout

`plot_cover_diagram` uses the module-level `COVER_POSITIONS`. To move a node,
build your own graph and pass a position dictionary to `networkx`:

```python
import matplotlib.pyplot as plt
import networkx as nx

from notes_order_theory import build_cover_graph

graph = build_cover_graph()
positions = {"a": (0, 1), "b": (1, 0), "c": (0, 3), "d": (2, 2), "e": (1, 4)}
nx.draw(graph, pos=positions, with_labels=True)
plt.savefig("out/cover_diagram.png")
```

## Format a different ground set

`latex_pairs` works for any iterable of strings:

```python
from notes_order_theory import latex_pairs

print(latex_pairs(["x", "y", "z"]))
```

## Write a figure to a custom path

Every plotting function takes an output path and creates its parent directory:

```python
from notes_order_theory import plot_cover_diagram

plot_cover_diagram("out/cover.png")
```
