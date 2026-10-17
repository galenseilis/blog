# moose-fp

Numerical solutions of general Fokker-Planck models of moose movement.

This package accompanies the blog post
[A General Fokker-Planck Model of Moose Movement](https://galenseilis.github.io/blog/posts/general-fokker-planck-moose-movement/).
It solves the Fokker-Planck equation

$$\frac{\partial p}{\partial t} = -\nabla \cdot (b[x,p]\,p) + \frac{1}{2}\,\partial_i \partial_j (D_{ij}(x)\,p) - \lambda(x)\,p$$

with a habitat potential, a spatially varying diffusion field, no-flux
barriers, a nonlocal interaction term, fractional diffusion, and coupled
behavioural states.

Two entry points reproduce the post's experiments:

- `moose-fp-2d` — the full general equation on a two-dimensional landscape
  with a river and a bridge, a variable diffusion field, and a comparison
  against the Boltzmann equilibrium.
- `moose-fp-beyond-gaussian` — three one-dimensional repairs of the
  Ornstein-Uhlenbeck model: fractional diffusion (power-law tails), nonlocal
  attraction (herd bunching), and behavioural states (bimodal utilization).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/general-fokker-planck-moose-movement"
```

Requires Python 3.11 or newer, and depends on `numpy`, `scipy`, and
`matplotlib`.

## Quick start

```python
import numpy as np
from moose_fp.general_fp_2d import build_domain, centre_delta, solve, steady_state
from moose_fp.numerics import total_variation

x, y, xx, yy, potential, solid = build_domain()
equilibrium = steady_state(potential, solid, 0.5)
start = centre_delta(x, y, 1.0, 2.0, solid)
p, dt, _saved, _open = solve(potential, solid, 0.5, start, t_end=10.0)
total_variation(p, equilibrium)  # distance to the Boltzmann equilibrium
```

```python
from moose_fp.beyond_gaussian_fp import fractional_ou

x, p, spacing, mass_drift = fractional_ou(
    alpha=0.5, n_steps=2000, dt=0.005, grid=1024, length=32.0
)
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
