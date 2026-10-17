# Explanation

## What a compound distribution is

A compound distribution lets one distribution's parameters be random variables
from other distributions. Instead of fixing the mean and scale of a normal at
numbers, we draw them from a normal and an exponential:

```text
X ~ Normal(2, 4)
L ~ Exponential(100)
N ~ Normal(X, L)
```

This is the probabilistic skeleton of a hierarchical (multilevel) model: a
population-level distribution over parameters, and a likelihood that conditions
on them.

## Why it is useful

Fixing a parameter at a point value pretends we know it exactly. Making it a
random variable carries the uncertainty through to predictions, which is what
Bayesian hierarchical modelling does systematically. SymPy's compound
distribution support lets you write the model down symbolically and then ask for
its density as a closed-form expression (here, a nested integral), rather than
committing to a sampler immediately.

## The trade-off

Symbolic density expressions grow quickly. The example's density is already a
double integral with no elementary antiderivative, so evaluating moments
symbolically may be slow or may not close at all. The practical division of
labour is to use SymPy to derive and understand the model, and a numerical
toolkit (or a probabilistic programming language) to fit it.

## Where to go next

- [Tutorial](tutorials.md)
- [How-to guides](how-to-guides.md)
