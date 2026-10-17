# Explanation

## Why tuples are a natural class identifier

A Ciw customer class is just a name. If classes are distinguished by a
collection of attributes — a customer type, a priority, a cohort, and so on —
then a tuple is the obvious encoding: it is immutable, so it cannot be mutated
out from under the simulation, and it carries several attributes in one object.
It is not a full-blown record type, but it is one syntactic step away from one.

## Why ordering is the constraint

Ciw does not merely use class names as dictionary keys; it *sorts* them. Sorting
requires a total order, and Python has no total order across mixed types. Tuple
comparison is lexicographic: it compares the first elements, and only if those
are equal does it compare the second elements. So `("Baby", 0)` against
`(1,)` fails immediately, because `"Baby"` and `1` are not comparable, even
though the second elements `0` and `1` would be.

Two properties therefore have to hold for a set of tuple class names:

1. every tuple can be compared with every other tuple, and
2. all tuples use comparable types at each position.

Tuples of different lengths are fine as long as the shared prefix is comparable
— lexicographic comparison stops at the end of the shorter tuple. The failure
comes from *types*, not from lengths.

## The padding fix, and its cost

The post's fix is to normalise the shape: make every tuple the same length and
give each position a consistent type, filling gaps with a sentinel such as the
empty string or `0`. This is simple and works, but it has a cost. The sentinel
is a lie — `""` and `0` are not real attribute values — and readers of the code
have to know that convention. If two different classes differ only in a padded
position, that is invisible in the tuple.

## The natural next step

Tuples are a good first start, as the post puts it, but the real need is a
data-containing class that is *immutable* and *ordered*. A frozen dataclass with
`order=True` gives exactly that: named fields that document the attributes, a
generated total order that Ciw can sort on, and immutability that the tuple
provides for free. That replaces the positional sentinel convention with named
fields, at the price of a little more code.
