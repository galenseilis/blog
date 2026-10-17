# Tutorial

This tutorial draws both figures from the post and generates the LaTeX ordered
pairs. It should take a couple of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-order-theory"
```

## 2. Draw the example partial order

The example partial order on `X = {a, b, c, d, e}` is reflexive, so its digraph
has a self-loop at every node:

```python
from notes_order_theory import plot_example_partial_order

plot_example_partial_order("figures/example_partial_order.png")
```

Edges run from the smaller element to the larger one, following the relation
`{(a, c), (a, e), (b, c), (b, d), (b, e), (d, e)}` plus the self-pairs.

## 3. Draw the cover diagram

The cover relation drops any pair that has an element strictly between its
ends. Here `(b, e)` is dropped because `b < d < e`:

```python
from notes_order_theory import plot_cover_diagram

plot_cover_diagram("figures/cover_diagram.png")
```

The nodes use fixed positions, so each edge points strictly upward, which is
what distinguishes a cover diagram from an arbitrary DAG drawing.

## 4. Generate LaTeX ordered pairs

Writing out all 25 pairs of a five-element set by hand is tedious:

```python
from notes_order_theory import latex_pairs

print(latex_pairs(("a", "b", "c", "d", "e")))
```

The output is a single LaTeX line such as
`\\{(a, a), (a, b), ..., (e, e)\\}` that you can paste straight into a
document. You now have everything the post produces; read the
[how-to guides](how-to-guides.md) to adapt it.
