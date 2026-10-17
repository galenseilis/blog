# API reference

## `sympy_compound_distributions.compound`

### `compound_distribution() -> CompoundDistribution`

Build and return the compound distribution from the post:

```text
X ~ Normal(2, 4)
L ~ Exponential(100)
N ~ Normal(X, L)
C = CompoundDistribution(N)
```

The returned object's `str` is
`CompoundDistribution(NormalDistribution(X, L))`, and its `pdf` is a nested
SymPy `Integral` over `X` and `L`.

### `main()`

Console-script entry point. Builds the distribution and prints it.

## `sympy_compound_distributions`

### `compound_distribution`

Re-export of `sympy_compound_distributions.compound.compound_distribution`.

## Console script

```text
sympy-compound-distributions
```

Prints:

```text
CompoundDistribution(NormalDistribution(X, L))
```
