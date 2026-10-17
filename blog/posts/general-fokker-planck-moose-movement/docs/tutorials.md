# Tutorial

This tutorial runs the general Fokker-Planck solver on the toy landscape and
then the one-dimensional repairs. It should take a few minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/general-fokker-planck-moose-movement"
```

## 2. Build the landscape

```python
from moose_fp.general_fp_2d import build_domain

x, y, xx, yy, potential, solid = build_domain()
```

`potential` is the habitat potential `U` (low values are good habitat) with two
wells, and `solid` marks the cells blocked by the river away from the bridge.

## 3. Predict the equilibrium

With a constant diffusion `D`, the stationary density is the Boltzmann
distribution `p ~ exp(-U/D)` on the open cells.

```python
from moose_fp.general_fp_2d import steady_state

equilibrium = steady_state(potential, solid, diffusion=0.5)
```

## 4. Integrate the equation

```python
from moose_fp.general_fp_2d import centre_delta, solve
from moose_fp.numerics import total_variation

start = centre_delta(x, y, 1.0, 2.0, solid)
p, dt, saved, open_cells = solve(potential, solid, 0.5, start, t_end=10.0)
print(dt, total_variation(p, equilibrium))
```

The density relaxes towards the equilibrium; the distance shrinks over time.

## 5. Tails, interaction, and switching in one dimension

```python
from moose_fp.beyond_gaussian_fp import fractional_ou, interaction_run

# Fractional diffusion gives power-law tails.
x1, p1, spacing, drift = fractional_ou(alpha=0.5, n_steps=2000, dt=0.005, grid=1024, length=32.0)

# Nonlocal attraction tightens the range.
x2, p_inter, t, change = interaction_run(0.6, grid=256, length=16.0, dt=0.01, t_end=50.0, width=0.5)
```

## 6. Reproduce the post's figures

```bash
moose-fp-2d                 # writes figures/general_fp_2d.png
moose-fp-beyond-gaussian    # writes figures/beyond_gaussian_fp.png
```

You have now exercised every mechanism in the post. Next, read the
[how-to guides](how-to-guides.md) for practical recipes.
