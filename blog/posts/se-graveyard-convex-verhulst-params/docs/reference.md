# API reference

## Symbols and function

### `se_graveyard_convex_verhulst_params.hessian.t`, `.p0`, `.k`, `.r`

SymPy symbols `t`, `p0`, `k`, and `r`.

### `se_graveyard_convex_verhulst_params.verhulst(t, p0, k, r)`

Return the Verhulst growth function
$k / (1 + (k - p_0)e^{-rt}/p_0)$.

### `se_graveyard_convex_verhulst_params.hessian.verhulst(t, p0, k, r)`

The same function, defined in the `hessian` module.

### `se_graveyard_convex_verhulst_params.hessian()`

Return the symbolic `sympy.Matrix` Hessian of the Verhulst function with respect
to `(p0, k, r)`.

### `se_graveyard_convex_verhulst_params.H`

The precomputed Hessian matrix, equal to `hessian()`.

## Eigenvalues

### `se_graveyard_convex_verhulst_params.eigenvalues`

Module-level binding of `H.eigenvals()`. Importing it forces the (expensive)
symbolic eigen-decomposition.

## Console script

### `se_graveyard_convex_verhulst_params.main.main()`

Print the Hessian `H`. Entry point for the console script.

| Command | Effect |
| --- | --- |
| `se-graveyard-convex-verhulst-params` | print the symbolic Hessian |
