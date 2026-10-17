# Tutorial

This tutorial builds a Ciw network whose customer classes are tuples and runs
it.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-tuple-class-names"
```

## 2. Build a tuple-named network

Each class name is a `(str, int)` tuple, and the class name keys the arrival,
service, and routing dictionaries:

```python
from ciw_tuple_class_names import tuple_keys

network = tuple_keys.build_network()
```

Here `("Baby", 0)` and `("Child", 1)` are the two classes. Because both tuples
have the same length and the same position-wise types, Python can order them
and Ciw is happy.

## 3. Run the simulation

```python
simulation = tuple_keys.run_simulation(max_time=9)
records = simulation.get_all_records()
print(len(records))
```

## 4. See the failure mode

Now build the network again, but rename `("Child", 1)` to `(1,)`. The first
elements are now a `str` and an `int`, and Ciw sorts its class names, so the
comparison fails:

```python
from ciw_tuple_class_names import mixed_types
import pandas as pd

try:
    mixed_types.build_network()
except TypeError as exc:
    print("TypeError:", exc)
```

## 5. Apply the fix

Pad the tuples so every position has a consistent type. Using the empty string
`""` where a name is not needed keeps the first element a `str`:

```python
from ciw_tuple_class_names import empty_string

network = empty_string.build_network()
simulation = empty_string.run_simulation(max_time=9)
print(len(simulation.get_all_records()))
```

You now know the whole workflow: build with tuples, watch the mixed-type case
fail, and pad to fix it. Next, read the [how-to guides](how-to-guides.md).
