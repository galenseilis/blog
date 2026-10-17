# How-to guides

## Run all three cases at once

```bash
ciw-tuple-class-names
```

The console script runs the two working networks and then reports the
`TypeError` from the mixed-type network.

## Reproduce the mixed-type failure in a test

```python
import pytest
from ciw_tuple_class_names import mixed_types

with pytest.raises(TypeError, match="not supported between instances"):
    mixed_types.build_network()
```

## Fix mixed types by padding

Give every tuple the same length and the same position-wise types. Replace a
missing name with an empty string and a missing number with `0`:

```python
("Baby", 0)   # name present, index present
("", 1)       # no name, index present
```

Both are `(str, int)`, so they order cleanly.

## Choose a tuple layout up front

Decide the length and the type of each position before adding classes. As soon
as one class uses an `int` where another uses a `str`, Ciw's sort fails. Keeping
one canonical shape avoids the problem entirely.

## Combine tuples with other orderable classes

Ciw only requires that class names be comparable. Tuples of consistently-typed
elements satisfy that requirement, which is why they are such a convenient
stand-in for a richer attribute class.
