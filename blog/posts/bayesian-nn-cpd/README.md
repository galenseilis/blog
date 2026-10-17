# bayesian-nn-cpd

Toy Bayesian rank-1 CP decomposition example using PyMC.

This package is extracted from the blog post
[Bayesian Non-Negative CPD](https://galenseilis.github.io/blog/posts/bayesian-nn-cpd/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/bayesian-nn-cpd"
```

Requires Python 3.11 or newer.

## Quick start

```python
from bayesian_nn_cpd.model import build_model, simulate_data

observed, size = simulate_data(size=3)
model = build_model(size=size, observed=observed)
```
