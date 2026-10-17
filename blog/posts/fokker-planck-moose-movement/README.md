# moose-ou

Simulation of, and Fokker-Planck solutions for, the Ornstein-Uhlenbeck model of
moose movement.

An Ornstein-Uhlenbeck (OU) process is a diffusion with a linear restoring force:
an animal is pulled back towards a home-range centre and buffeted by random
motion. It is the special case of the general Fokker-Planck framework in which
the density stays Gaussian and every quantity of interest is available in closed
form.

This repository contains two coupled packages from the blog post
[The Ornstein-Uhlenbeck Model of Moose Movement](https://galenseilis.github.io/blog/posts/fokker-planck-moose-movement/):

- **`moose_ou`** (Rust, this directory): simulates a virtual population of moose
  as two-dimensional OU processes with an Euler-Maruyama scheme and writes
  `data/moose_positions.csv` and `data/moose_track.csv`.
- **`moose-ou-fp`** (Python, [`python/`](python)): solves the one-dimensional
  Fokker-Planck equation for the same model on a grid and compares the result
  against the simulated moose and the analytic Gaussian.

The density of the positions obeys the Fokker-Planck equation

```text
dp/dt = kappa d/dx[(x - c) p] + (sigma^2 / 2) d^2p/dx^2
```

whose stationary solution is `Normal(c, sigma / sqrt(2 kappa))` per axis.

## Install

The Python package is installable straight from GitHub:

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/fokker-planck-moose-movement/python"
```

The Rust crate is built from this directory:

```bash
cargo build --release
```

## Quick start

Run the simulation, which prints a comparison of the simulated moments with the
analytic values and writes the CSVs:

```bash
cargo run --release
```

Then solve the density equation, reproduce the figure, and print the
Fokker-Planck-versus-analytic diagnostics:

```bash
moose-ou-fp            # writes figures/moose_fokker_planck.png
```

Run the test suites with `cargo test` and
`uv run --project python --group dev pytest`.

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
