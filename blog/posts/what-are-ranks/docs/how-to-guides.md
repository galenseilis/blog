# How-to guides

## Rank a sample with only one method

```python
from scipy.stats import rankdata

rankdata([3, 3, 4, 5], method="dense")  # array([1., 1., 2., 3.])
```

The `method` argument is one of `average`, `min`, `max`, `dense`, or `ordinal`.

## Compare all five methods at once

```python
from what_are_ranks import rank_table

rank_table([3, 3, 4, 5])
```

## Rank in reverse order

`rankdata` itself only ranks ascending. Negate the data first to reverse it:

```python
from scipy.stats import rankdata

rankdata([-v for v in [3, 3, 4, 5]])
```

`pandas.DataFrame.rank` offers the same idea through its `ascending=False`
argument.

## Control the random sample

```python
from what_are_ranks import sample_binomial

sample_binomial(seed=123, size=25, trials=10, p=0.5)
```

Pass `seed=None` for a non-reproducible sample.

## Handle percentile ranks

Percentile ranks are not produced by `rankdata`; use
`scipy.stats.percentileofscore`, or `pandas.DataFrame.rank(pct=True)`.
