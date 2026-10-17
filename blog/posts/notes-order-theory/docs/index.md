# notes-order-theory documentation

`notes-order-theory` contains the drawings and the LaTeX helper from the blog
post *Notes on Order Theory*. It has three jobs:

- Draw the digraph of the example partial order, including the self-loops that
  come from reflexivity.
- Draw the cover diagram of the example strict partial order, with nodes
  placed so every edge points upward.
- Generate the LaTeX source for the full Cartesian product `X x X`.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): draw both figures and generate the LaTeX pairs.
- [How-to guides](how-to-guides.md): customise the relation, positions, and
  output paths.
- [Reference](reference.md): the public API and the console script.
- [Explanation](explanation.md): partial orders, cover relations, and why the
  cover diagram looks the way it does.
