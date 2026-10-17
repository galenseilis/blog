# ciw-simpy-bank-renege

A Ciw implementation of SimPy's Bank Renege example.

SimPy's Bank Renege example is an M/M/1 queue with two twists: there are a
fixed number of customers, and waiting customers give up (renege) after a
uniformly distributed patience time. This package builds that model in Ciw,
where reneging is supported directly, and estimates the distribution of the
total sojourn time by fitting a Gamma distribution to a large number of
simulations.

This package is the code from the blog post
[A Ciw Implementation of SimPy's Bank Renege Example](https://galenseilis.github.io/blog/posts/ciw-simpy-bank-renege/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-simpy-bank-renege"
```

Requires Python 3.11 or newer, and depends on `ciw`, `numpy`, `scipy`, and
`matplotlib`.

## Quick start

```python
from ciw_simpy_bank_renege import network

simulation = network.run_simulation()
[record.exit_date for record in simulation.get_all_records()]
```

Run the console script to simulate one million times and save the
fitted-density plot:

```bash
ciw-simpy-bank-renege
```

The plot is written to `figures/bank-renege-run-times.png`.

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
