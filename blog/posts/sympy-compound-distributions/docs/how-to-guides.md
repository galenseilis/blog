# How-to guides

## Build the post's exact distribution

```python
from sympy_compound_distributions import compound_distribution

compound_distribution()  # CompoundDistribution(NormalDistribution(X, L))
```

## Build your own compound distribution directly

`compound_distribution()` is a convenience wrapper for the example in the post.
To use different parameters, assemble the pieces with SymPy:

```python
from sympy.stats import Exponential, Normal
from sympy.stats.compound_rv import CompoundDistribution
from sympy.stats.crv_types import NormalDistribution

mean = Normal("mean", 0, 1)
scale = Exponential("scale", 10)
CompoundDistribution(NormalDistribution(mean, scale))
```

## Evaluate the density at a point

```python
compound = compound_distribution()
compound.pdf(0)
```

The result is an unevaluated nested `Integral` over `X` and `L`.

## Check the type

```python
from sympy.stats.compound_rv import CompoundDistribution

assert isinstance(compound_distribution(), CompoundDistribution)
```
