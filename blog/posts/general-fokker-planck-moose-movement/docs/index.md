# moose-fp documentation

`moose-fp` solves general Fokker-Planck equations for animal movement
numerically. It is the code behind the blog post
[A General Fokker-Planck Model of Moose Movement](https://galenseilis.github.io/blog/posts/general-fokker-planck-moose-movement/),
which repairs, one term at a time, the defects of the Ornstein-Uhlenbeck model
from the [previous post](https://galenseilis.github.io/blog/posts/fokker-planck-moose-movement/).

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## What is here

- **`moose_fp.general_fp_2d`** — the general equation on a two-dimensional
  landscape: a habitat potential with two wells, a river with a bridge, a
  spatially varying diffusion field, and an optional nonlocal interaction.
- **`moose_fp.beyond_gaussian_fp`** — three one-dimensional repairs: fractional
  diffusion, nonlocal attraction, and behavioural states.
- **`moose_fp.numerics`** — a small shared helper for total-variation distance.
