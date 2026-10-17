# Tutorial

## 1. Draw the post's sample

```python
from what_are_ranks import sample_binomial

x = sample_binomial()
list(x)
```

The sample is drawn from `Binomial(10, 0.5)` with a fixed seed, so it always
comes out the same.

## 2. Rank it

```python
from what_are_ranks import rank_table

table = rank_table(x)
print(table.to_string(index=False))
```

Because the sample has ties (several values repeat), the five methods disagree:
the `average` method returns fractional ranks, while `min`, `max`, `dense`, and
`ordinal` return integers with different spacing.

## 3. Run it from the command line

```bash
what-are-ranks
```

## 4. Where to go next

- [How-to guides](how-to-guides.md) to rank your own data.
- [Reference](reference.md) for the full API.
