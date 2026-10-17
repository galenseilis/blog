# Tutorial

This tutorial builds up the two halves of the project from scratch: a particle
simulation of the Ornstein-Uhlenbeck process, and a direct solution of the
Fokker-Planck equation that those particles obey.

## 1. Simulate a virtual population (Rust)

Every virtual moose starts at the home-range centre and takes an
Euler-Maruyama step each time increment:

```text
x <- x - kappa (x - c) dt + sigma dW
```

where `dW` is a Wiener increment with variance `dt`. In Rust the whole model is
driven by a `MooseConfig`:

```rust
use moose_ou::{MooseConfig, simulate, summarise};

let config = MooseConfig {
    kappa: 0.5,
    sigma: 1.0,
    dt: 0.01,
    steps: 2_000,
    moose: 10_000,
    centre: 0.0,
    seed: 20_261_016,
};

let positions = simulate(&config);
let summary = summarise(&config, &positions);
println!("simulated sd x: {:.3} km", summary.sd_x);
```

Run the full program with `cargo run --release`. It prints a table comparing the
simulated moments with the analytic values and writes the CSVs that the Python
half reads.

## 2. Check the moments against the analytics

The stationary standard deviation is available in closed form:

```rust
let sd = config.stationary_sd();       // sigma / sqrt(2 kappa)
let radius = config.mean_radius();     // sd * sqrt(pi / 2)
```

For the defaults, `kappa = 0.5 1/h` and `sigma = 1 km/sqrt(h)` give `sd = 1 km`
and a mean radius of about `1.253 km`. The simulation should reproduce both to
within a percent.

## 3. Solve the density equation (Python)

The Python package integrates the Fokker-Planck equation

```text
dp/dt = kappa d/dx[(x - c) p] + (sigma^2 / 2) d^2p/dx^2
```

on a grid, starting from a point mass at the centre:

```python
from moose_ou_fp import solve_fokker_planck, diagnostics

x, times, snapshots, masses, means, variances = solve_fokker_planck(
    extent=5.0, dx=0.05, dt=1e-3, t_end=2.0
)
print(diagnostics(masses, means, variances, t_end=2.0))
```

Mass stays at one by construction, and the variance relaxes towards
`sigma**2 / (2 kappa)` like `1 - exp(-2 kappa t)`.

## 4. Put the two halves together

With the CSVs written by the Rust program, the console script overlays the
particles, the PDE solution, and the analytic density in a single figure:

```bash
cargo run --release
moose-ou-fp
```

That is the figure in the blog post, and the printed diagnostics are the
comparison table quoted there.
