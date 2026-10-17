# moose-ellipse documentation

`moose-ellipse` computes **potential path areas** for animals tracked with GPS
collars. Given two fixes and a maximum speed, it builds the ellipse of places
the animal could have occupied in between, and it can test whether two animals
could have met in space *and* time.

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): build your first reachable ellipse and a
  two-animal co-occurrence test.
- [How-to guides](how-to-guides.md): reproduce the figures, handle infeasible
  fixes, and work with projected coordinates.
- [Reference](reference.md): the public API.
- [Explanation](explanation.md): why the reachable region is an ellipse, and
  what the method does and does not claim.
