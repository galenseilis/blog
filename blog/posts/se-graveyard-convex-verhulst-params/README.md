# se-graveyard-convex-verhulst-params

Symbolic Hessian of the Verhulst (logistic) growth function with respect to its
parameters.

The Verhulst model is
$p(t) = \frac{k}{1 + (k - p_0)e^{-rt}/p_0}$. This package uses SymPy to build the
$3 \times 3$ Hessian of $p$ with respect to $k$, $p_0$, and $r$, which is the
first step in asking whether the function is convex in its parameters.

This package is the code from the blog post
[Is the Verhulst (logistic) growth function convex over its parameters?](https://galenseilis.github.io/blog/posts/se-graveyard-convex-verhulst-params/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/se-graveyard-convex-verhulst-params"
```

Requires Python 3.11 or newer and depends on `numpy` and `sympy`.

## Quick start

```python
from se_graveyard_convex_verhulst_params import H

print(H.shape)          # (3, 3)
print(H[1, 1])          # second derivative wrt p0
```

## Docs

Start at [`docs/index.md`](docs/index.md).
