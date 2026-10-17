# Tutorial

## 1. Build the model

The post describes three layers: a normal mean, an exponential scale, and a
normal variable whose parameters are those two random variables.

```python
from sympy_compound_distributions import compound_distribution

compound = compound_distribution()
```

The result is a `CompoundDistribution` wrapping a `NormalDistribution`:

```text
CompoundDistribution(NormalDistribution(X, L))
```

## 2. Inspect the result

```python
str(compound)  # 'CompoundDistribution(NormalDistribution(X, L))'
type(compound).__name__  # 'CompoundDistribution'
```

## 3. Evaluate the density

```python
compound.pdf(0)
```

This returns a nested SymPy `Integral`: the outer integral is over the scale
`L`, and the inner integral is over the mean `X`.

## 4. Where to go next

- [How-to guides](how-to-guides.md) for changing the parameters.
- [Reference](reference.md) for the full API.
