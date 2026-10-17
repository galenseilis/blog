# API reference

## `notes_order_theory.partial_order`

- `EXAMPLE_ORDER`: the example relation as a list of two-character strings,
  `["aa", "ac", "ae", "bb", "bc", "bd", "be", "cc", "dd", "de", "ee"]`.
- `build_digraph(order=None) -> networkx.DiGraph`: build the digraph of a
  relation given as two-character pairs. Defaults to `EXAMPLE_ORDER`.
- `plot_example_partial_order(output="figures/example_partial_order.png") -> pathlib.Path`:
  draw the example digraph and save it. Parent directories are created.
- `main()`: console entry point that draws the example digraph.

## `notes_order_theory.cover_diagram`

- `COVER_POSITIONS`: fixed node positions for the example cover diagram.
- `COVER_EDGES`: the cover pairs of the example order.
- `build_cover_graph(edges=None) -> networkx.Graph`: build the cover graph.
  Defaults to `COVER_EDGES`.
- `plot_cover_diagram(output="figures/cover_diagram.png") -> pathlib.Path`:
  draw the cover diagram and save it.
- `main()`: console entry point that draws the cover diagram.

## `notes_order_theory.latex_pairs`

- `latex_pairs(elements) -> str`: return the LaTeX source for every ordered
  pair of `elements`, as produced by the post's snippet.
- `main()`: print the pairs for `("a", "b", "c", "d", "e")`.

## `notes_order_theory.figures`

- `render_all(output_dir="figures") -> list[pathlib.Path]`: render both post
  figures and return the written paths.
- `main()`: console-script entry point.

## Console scripts

| Command | Writes |
| --- | --- |
| `notes-order-theory` | `figures/example_partial_order.png`, `figures/cover_diagram.png` |
