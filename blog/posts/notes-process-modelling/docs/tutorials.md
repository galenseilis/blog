# Tutorial

This tutorial builds a labelled transition system and takes its synchronous
product with another. It should take a couple of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-process-modelling"
```

## 2. Describe one system

A labelled transition system is described by its states, its actions, its
transitions, an initial state, and its accepting (final) states.

```python
from notes_process_modelling import LTS

lts1 = LTS(
    ["s1", "s2"],                                # states
    ["a", "b"],                                  # actions
    {"s1": {"a": "s2", "b": "s1"},               # transitions
     "s2": {"a": "s1", "b": "s2"}},
    "s1",                                        # initial state
    ["s2"],                                      # accepting states
)
```

`transitions[s][a]` is the state reached from `s` by taking action `a`.

## 3. Describe a second system

```python
lts2 = LTS(
    ["s3", "s4"],
    ["a", "c"],
    {"s3": {"a": "s4", "c": "s3"},
     "s4": {"a": "s3", "c": "s4"}},
    "s3",
    ["s4"],
)
```

The two systems share the action `a` and nothing else.

## 4. Take the synchronous product

The product couples the systems on their shared actions. Its states are the
pairs of states, its actions are the actions both systems can take, and it has
a transition only when *both* components can take that action.

```python
product = lts1 * lts2
print(product.S)                 # ['s1s3', 's1s4', 's2s3', 's2s4']
print(product.A)                 # {'a'}
print(product.transitions)
print(product.initial_state)     # 's1s3'
print(product.accepting_states)  # ['s2s4']
```

The private actions `b` and `c` are absent from the product because neither is
shared. Run the console script to see the same output:

```bash
notes-process-modelling
```

You now know the whole workflow. Next, read the
[how-to guides](how-to-guides.md) for building larger products.
