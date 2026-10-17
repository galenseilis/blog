# Tutorial

This tutorial builds the Hessian of the Verhulst growth function. It should take
a few minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/se-graveyard-convex-verhulst-params"
```

## 2. The function and its symbols

The module `hessian` defines the symbols `t`, `p0`, `k`, and `r`.

```python
from se_graveyard_convex_verhulst_params import verhulst
from se_graveyard_convex_verhulst_params.hessian import r, t, p0, k

p = verhulst(t, p0, k, r)
p
```

## 3. The Hessian

`hessian()` differentiates `p` twice with respect to every ordered pair of
`(p0, k, r)` and assembles the results into a SymPy `Matrix`.

```python
from se_graveyard_convex_verhulst_params import hessian

H = hessian()
print(H.shape)
```

The module also exposes the precomputed matrix as `H`.

```python
from se_graveyard_convex_verhulst_params import H

H
```

## 4. Eigenvalues

`eigenvals()` on the matrix gives the characteristic-polynomial roots, which are
what you check to decide definiteness.

```python
eigenvalues = H.eigenvals()
print(len(eigenvalues))
```

The eigenvalues are enormous expressions, which is exactly the point of the
post: a closed-form answer is not convenient here.

Continue with the [how-to guides](how-to-guides.md) to evaluate the Hessian
numerically.
