# sympy-compound-distributions

Build SymPy's compound distribution for a normal variable whose parameters are
themselves random variables:

```text
X ~ Normal(2, 4)
L ~ Exponential(100)
N ~ Normal(X, L)
```

This package is the code from the blog post
[SymPy Supports Compound Distributions](https://galenseilis.github.io/blog/posts/sympy-compound-distributions/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/sympy-compound-distributions"
```

Requires Python 3.11 or newer. The only dependency is `sympy`.

## Quick start

```python
from sympy_compound_distributions import compound_distribution

compound = compound_distribution()
compound  # CompoundDistribution(NormalDistribution(X, L))
compound.pdf(0)  # nested integral over X and L
```

Or from the command line:

```bash
sympy-compound-distributions
```

```text
CompoundDistribution(NormalDistribution(X, L))
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
