# API reference

## Rust crate: `moose_ou`

### `moose_ou::MooseConfig`

Movement-model parameters:

| Field | Type | Meaning |
| --- | --- | --- |
| `kappa` | `f64` | Home-range fidelity, in 1/h |
| `sigma` | `f64` | Exploratory jitter, in km/sqrt(h) |
| `dt` | `f64` | Time step, in h |
| `steps` | `usize` | Number of time steps |
| `moose` | `usize` | Number of virtual moose |
| `centre` | `f64` | Home-range centre, in km |
| `seed` | `u64` | Seed for reproducibility |

`MooseConfig::default()` returns the post parameters: `kappa = 0.5`,
`sigma = 1.0`, `dt = 0.01`, `steps = 2000`, `moose = 10_000`, `centre = 0.0`,
`seed = 20_261_016`.

### `MooseConfig::t_end() -> f64`

Total simulated time, `dt * steps`, in hours.

### `MooseConfig::stationary_sd() -> f64`

Analytic stationary standard deviation per axis, `sigma / sqrt(2 kappa)`.

### `MooseConfig::mean_radius() -> f64`

Analytic mean distance from the centre at stationarity, `stationary_sd() *
sqrt(pi / 2)`.

### `moose_ou::simulate(config: &MooseConfig) -> Vec<(f64, f64)>`

Simulate the final `(x, y)` position of every virtual moose.

### `moose_ou::summarise(config: &MooseConfig, positions: &[(f64, f64)]) -> Summary`

Compute the sample means, standard deviations, and mean radius, alongside the
analytic references. `Summary` has the fields `mean_x`, `mean_y`, `sd_x`,
`sd_y`, `mean_radius`, `centre`, `stationary_sd`, and `mean_radius_analytic`.

### `moose_ou::histogram(positions: &[(f64, f64)], min: f64, max: f64, bins: usize) -> Vec<usize>`

Count positions whose x coordinate lies in each of `bins` equal bins on
`[min, max)`.

### `moose_ou::run_with_config(config: &MooseConfig) -> std::io::Result<()>`

Simulate, print the summary and histogram, and write
`data/moose_positions.csv` and `data/moose_track.csv`.

### `moose_ou::run() -> std::io::Result<()>`

`run_with_config` with `MooseConfig::default()`. This is what the
`moose_ou` binary calls.

## Python package: `moose_ou_fp`

### Constants

`KAPPA = 0.5`, `SIGMA = 1.0`, `T_END = 20.0`, `CENTRE = 0.0`.

### `moose_ou_fp.load_positions(path) -> (x, y)`

Load the final `(x, y)` positions of every moose from a CSV with a header.

### `moose_ou_fp.load_track(path) -> (t, x, y)`

Load a representative `(t, x, y)` trajectory from a CSV with a header.

### `moose_ou_fp.analytic_variance(t, *, kappa=KAPPA, sigma=SIGMA) -> float`

Variance of the OU process started at the centre,
`sigma**2 / (2 kappa) * (1 - exp(-2 kappa t))`.

### `moose_ou_fp.stationary_sd(*, kappa=KAPPA, sigma=SIGMA) -> float`

Stationary standard deviation per axis, `sigma / sqrt(2 kappa)`.

### `moose_ou_fp.analytic_pdf(x, t, *, kappa=KAPPA, sigma=SIGMA, centre=CENTRE)`

Transition density of the OU process at time `t`.

### `moose_ou_fp.solve_fokker_planck(extent=5.0, dx=0.01, dt=5e-5, *, kappa=KAPPA, sigma=SIGMA, t_end=T_END, centre=CENTRE)`

Solve the 1D Fokker-Planck equation on the grid with an explicit finite-volume
scheme (upwinded drift, centred diffusion, no-flux walls). Returns the tuple
`(x, times, snapshots, masses, means, variances)`.

### `moose_ou_fp.diagnostics(masses, means, variances, *, kappa=KAPPA, sigma=SIGMA, t_end=T_END, centre=CENTRE) -> dict`

Compare the PDE solution at `t_end` with the analytic values. The returned dict
has keys `mass`, `pde_variance`, `analytic_variance`, `pde_mean`, and
`analytic_mean`.

### `moose_ou_fp.print_diagnostics(diag)`

Print the PDE-versus-analytic comparison quoted in the blog post.

### `moose_ou_fp.plot_comparison(x_positions, y_positions, t_track, x_track, y_track, solve, output, *, kappa=KAPPA, sigma=SIGMA, t_end=T_END, centre=CENTRE) -> Path`

Render the four-panel figure (trajectory, final positions, marginal density,
variance relaxation) and return the written path.

### `moose_ou_fp.run(positions_path="data/moose_positions.csv", track_path="data/moose_track.csv", output="figures/moose_fokker_planck.png") -> Path`

Load the CSVs, solve, plot, print the diagnostics, and return the written path.

## Console scripts

| Command | Writes |
| --- | --- |
| `moose-ou-fp` | `figures/moose_fokker_planck.png` |
| `cargo run --release` | `data/moose_positions.csv`, `data/moose_track.csv` |
