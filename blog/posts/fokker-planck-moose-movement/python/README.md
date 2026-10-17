# moose-ou-fp

Fokker-Planck and analytic solutions of the Ornstein-Uhlenbeck moose movement
model.

This is the Python half of the blog post
[The Ornstein-Uhlenbeck Model of Moose Movement](https://galenseilis.github.io/blog/posts/fokker-planck-moose-movement/).
The companion Rust crate `moose_ou`, which simulates the virtual moose, lives
in the parent directory and writes `data/moose_positions.csv` and
`data/moose_track.csv` for this package to read.

The package solves the 1D Fokker-Planck equation for the OU model on a grid
with an explicit finite-volume scheme and compares the result against the
simulated moose and the closed-form transition density.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/fokker-planck-moose-movement/python"
```

Requires Python 3.11 or newer, and depends on `numpy` and `matplotlib`.

## Quick start

Run the Rust crate first, then the console script from the post directory:

```bash
cargo run --release   # writes data/moose_positions.csv and data/moose_track.csv
moose-ou-fp           # writes figures/moose_fokker_planck.png and prints diagnostics
```

## Documentation

The package documentation, including a tutorial, how-to guides, an API
reference, and an explanation, lives in [`../docs`](../docs/index.md).

## License

Released for reuse with attribution to the original blog post.
