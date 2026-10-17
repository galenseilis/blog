# How-to guides

## Evaluate the Hessian at numeric parameter values

Substitute values for `t`, `p0`, `k`, and `r`, then convert to a numeric matrix.

```python
from se_graveyard_convex_verhulst_params import H
from se_graveyard_convex_verhulst_params.hessian import r, t, p0, k

subs = {t: 1.0, p0: 1.0, k: 10.0, r: 0.5}
Hn = H.subs(subs)
print([[float(H[i, j]) for j in range(3)] for i in range(3)])
```

## Check definiteness at a point

Use the signs of the eigenvalues of the numeric Hessian.

```python
import numpy as np

from se_graveyard_convex_verhulst_params import H
from se_graveyard_convex_verhulst_params.hessian import r, t, p0, k

Hn = H.subs({t: 1, p0: 1, k: 4, r: 1}).evalf()
M = np.array(Hn.tolist(), dtype=float)
print(np.linalg.eigvals(M))
```

The model is convex in the parameters at this point only if the eigenvalues are
all non-negative.

## Compute a single second derivative

Use SymPy directly on `verhulst`.

```python
from sympy import diff

from se_graveyard_convex_verhulst_params import verhulst
from se_graveyard_convex_verhulst_params.hessian import r, t, p0, k

diff(verhulst(t, p0, k, r), p0, 2)
```

## Reproduce the Hessian for another parameterisation

Reuse the recipe with your own expression: define symbols, build the matrix with
a nested loop of `diff`, and wrap it in `Matrix`.
