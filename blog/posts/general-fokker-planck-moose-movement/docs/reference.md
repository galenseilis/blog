# API reference

## `moose_fp.general_fp_2d`

Two-dimensional general Fokker-Planck solver with a habitat potential, a
diffusion field, no-flux barriers, and an optional nonlocal interaction.

### Constants

- `LENGTH = 4.0` km — domain side length.
- `GRID = 81` — cells per side.
- `D0 = 0.5` — base diffusion, km^2/h.
- `DEPTH = 2.0` — habitat well depth.
- `WIDTH = 0.5` — habitat well width, km.

### `build_domain(length=LENGTH, grid=GRID, depth=DEPTH, well_width=WIDTH)`

Return `(x, y, xx, yy, potential, solid)` for the toy landscape with two
Gaussian wells and a river at `x = 2` km crossed by a single bridge.

### `steady_state(potential, solid, diffusion, weights=None)`

Return the Boltzmann prediction `p ~ exp(-U/D)` on the open cells, normalised.

### `solve(potential, solid, diffusion, p0, t_end, interaction=0.0, record_times=())`

Explicit finite-volume integration. `diffusion` is a scalar or a 2-D array.
Returns `(p, dt, saved, open_)`, where `saved` maps each requested record time
to a density snapshot.

### `face_flux(p, drift, diffusion, solid, axis, spacing)`

Advective (upwinded) plus diffusive flux on cell faces.

### `divergence_from_flux(flux_x, flux_y, spacing)`

Divergence of a face-centred flux on a cell-centred grid.

### `gradient(field, spacing)`

Central gradient with second-order edges.

### `smooth(field)`

Gaussian smoothing used for the nonlocal interaction term.

### `centre_delta(x, y, cx, cy, solid)`

Normalised point mass at the grid node nearest `(cx, cy)`.

### `run(output="figures/general_fp_2d.png")`

Run the three experiments, print diagnostics, write the figure, and return the
written `Path`.

## `moose_fp.beyond_gaussian_fp`

One-dimensional repairs of the Ornstein-Uhlenbeck model.

### Constants

- `ALPHA = 0.5` — fractional order of the diffusion operator divided by two.
- `KAPPA = 1.0` — OU fidelity, 1/h.
- `DIFFUSION = 1.0` — diffusion coefficient, km^2/h.

### `fractional_ou(alpha, n_steps, dt, grid, length)`

Stationary density of the fractional OU process on a periodic domain via a
conservative split scheme. Returns `(x, p, spacing, mass_drift)`.

### `flow_contract(p, x, a)`

Push cell masses through the exact OU contraction `x -> x/a`, conserving mass.

### `advance_periodic(p, drift, spacing, diffusion, dt)`

Conservative explicit step for `dp/dt = -d/dx(b p) + d^2(D p)/dx^2` on a
periodic domain.

### `interaction_run(chi, grid, length, dt, t_end, width, tolerance=1e-10)`

Equilibrium with a nonlocal attraction towards the density. Returns
`(x, p, elapsed_time, final_change)`.

### `self_consistent_variance(chi, width, iterations=400)`

Fixed point of `v = D / (kappa + chi / (v + width^2))` for a Gaussian.

### `switch_run(x, spacing, dt, t_end, snapshot_at)`

Time-dependent solution of the two coupled behavioural-state equations.
Returns a dict mapping each snapshot time to `(p_a, p_b)`.

### `sample_path(grid_dt, t_end, seed=20261016)`

One representative switching path. Returns `(times, position, states)`.

### `run(output="figures/beyond_gaussian_fp.png")`

Run the three repairs, print diagnostics, write the figure, and return the
written `Path`.

## `moose_fp.numerics`

### `total_variation(p, q, spacing=1.0)`

Total-variation distance between two densities, optionally scaled by the grid
cell width.

## Console scripts

| Command | Writes |
| --- | --- |
| `moose-fp-2d` | `figures/general_fp_2d.png` |
| `moose-fp-beyond-gaussian` | `figures/beyond_gaussian_fp.png` |
