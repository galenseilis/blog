# How-to guides

Practical recipes for common tasks.

## Reproduce the figures from the blog post

```bash
moose-fp-2d
moose-fp-beyond-gaussian
```

Each writes a PNG into `figures/`. To choose a different path, call the `run`
functions directly:

```python
from moose_fp.general_fp_2d import run as run_2d
from moose_fp.beyond_gaussian_fp import run as run_beyond

run_2d("out/general_fp_2d.png")
run_beyond("out/beyond_gaussian_fp.png")
```

## Compare the solver against the Boltzmann equilibrium

Set up a constant diffusion, solve to a long time, and measure the distance to
`exp(-U/D)`:

```python
from moose_fp.general_fp_2d import build_domain, centre_delta, solve, steady_state
from moose_fp.numerics import total_variation

x, y, xx, yy, potential, solid = build_domain()
equilibrium = steady_state(potential, solid, 0.5)
start = centre_delta(x, y, 1.0, 2.0, solid)
p, dt, saved, open_cells = solve(potential, solid, 0.5, start, t_end=60.0)
print(total_variation(p, equilibrium))
```

The residual is dominated by the first-order upwinding of the drift, which adds
an artificial diffusion of size roughly `|b| * dx / 2`. Refine the grid to see
the first-order convergence.

## Add a nonlocal interaction to the two-dimensional solver

Pass an `interaction` strength to `solve`. The drift gains the term
`-chi * grad(G * p)`, pulling the density towards its own smoothed mass:

```python
from moose_fp.general_fp_2d import build_domain, centre_delta, solve

x, y, xx, yy, potential, solid = build_domain()
start = centre_delta(x, y, 1.0, 2.0, solid)
p, dt, saved, open_cells = solve(potential, solid, 0.5, start, t_end=10.0, interaction=0.2)
```

## Predict the interacting variance in one dimension

For a Gaussian density the self-consistency condition closes, and
`self_consistent_variance` returns its fixed point:

```python
from moose_fp.beyond_gaussian_fp import self_consistent_variance

print(self_consistent_variance(0.0, width=0.5))  # 1.0, the free case
print(self_consistent_variance(0.6, width=0.5))  # tighter
```

## Work with a finer grid

`build_domain` accepts `length` and `grid`. The solver reads the domain side
length from the module constant `LENGTH`, so set it to match if you change the
domain size, or keep the default `4 x 4` km landscape and increase only the
resolution.
