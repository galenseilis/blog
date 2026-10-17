# How-to guides

## Reproduce the blog post figure

From the post directory:

```bash
cargo run --release   # writes data/moose_positions.csv and data/moose_track.csv
moose-ou-fp           # writes figures/moose_fokker_planck.png
```

`moose-ou-fp` must be run from the post directory so that the relative `data/`
and `figures/` paths resolve. Install it first with

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/fokker-planck-moose-movement/python"
```

## Change the movement parameters

Edit the `MooseConfig` values in `src/lib.rs` (or build your own):

```rust
use moose_ou::{MooseConfig, run_with_config};

let config = MooseConfig {
    kappa: 0.25,     // weaker fidelity: a four-hour memory
    sigma: 2.0,      // more restlessness
    ..MooseConfig::default()
};
run_with_config(&config).unwrap();
```

Then update the matching constants in the Python module
(`KAPPA`, `SIGMA`, `T_END`, `CENTRE`) so that both halves describe the same
process.

## Tune the finite-volume grid

`solve_fokker_planck` exposes the numerical knobs directly:

```python
solve_fokker_planck(extent=8.0, dx=0.005, dt=2e-5, t_end=20.0)
```

Halving `dx` roughly halves the artificial diffusion `|v| dx / 2` introduced by
upwinding, at the cost of four times the memory and twice the step count for a
fixed `dt`. Reduce `dt` too if the scheme becomes unstable; the explicit update
is stable when `dt` is small relative to `dx**2 / (2 * diffusivity)`.

## Run the tests

```bash
cargo test                                  # Rust
uv run --project python --group dev pytest  # Python
```

The Python tests use coarse grids so that the whole suite runs in a few seconds.

## Simulate a single track instead of a population

`write_track` in `src/lib.rs` re-seeds the generator and records one
representative trajectory, subsampled every ten steps. Copy that pattern to
produce a single path highlighted against the population.
