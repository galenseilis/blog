# How-to guides

Task recipes for working with labelled transition systems.

## Reproduce the worked example

The example from the blog post is available as a function:

```python
from notes_process_modelling import synchronous_product_demo

product = synchronous_product_demo()
print(product.S)
print(product.A)
```

Run the console script `notes-process-modelling` to print the product's states,
actions, transitions, initial state, and accepting states.

## Build a product of several systems

The product is associative, so it can be applied repeatedly:

```python
from notes_process_modelling import synchronous_product_demo
from notes_process_modelling.lts import LTS

third = LTS(["t1"], ["a"], {"t1": {"a": "t1"}}, "t1", ["t1"])
product = synchronous_product_demo() * third
print(product.A)
```

Because the product only ever exposes the *intersection* of action sets, adding
a system with no shared actions produces a product whose action set is empty.

## Understand why a state pair is missing

The product only includes a transition when both operands can take the same
action from their current states. If a transition you expected does not appear,
check whether the action is present in *both* the operands' transition
dictionaries.

## Guard against non-LTS operands

`__mul__` raises `TypeError` when the right-hand operand is not an `LTS`. This
makes accidental multiplication by a number fail loudly instead of silently
producing nonsense:

```python
from notes_process_modelling.example import build_lts1

try:
    build_lts1() * 3
except TypeError as exc:
    print("not an LTS:", exc)
```

## Keep states hashable and addable

The product builds new state labels by adding the two component labels
(`s1 + s2`). The reference implementation uses strings; if you pass another
type, make sure `+` is defined for it.
