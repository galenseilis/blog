# notes-differential-forms documentation

`notes-differential-forms` contains the figures from the blog post *Notes on
Differential Forms*. Each figure makes a different point about tangent spaces:

- On the cubic `y = x**3 - 10x`, the tangent space at `(2, -12)` is the set of
  tangent vectors spanned by `(1, f'(a))`, and the figure marks the point, the
  slope, and the pullbacks onto the coordinate axes.
- On the parabola `y = x**2`, the same construction at `(1, 1)` shows how
  `dy = 2a dx` recovers the derivative.
- The differential-axes figure draws a tangent vector `<c, d>` against the
  axes `dx` and `dy`, which is the picture behind treating `dx` and `dy` as a
  basis of the cotangent space.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): render your first tangent-space figure and all of
  the post's figures.
- [How-to guides](how-to-guides.md): choose output paths, embed the figures,
  and customise them.
- [Reference](reference.md): the public API and the console script.
- [Explanation](explanation.md): what the figures show and how the pieces fit
  together in differential-geometry terms.
