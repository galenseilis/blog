# ciw-tuple-class-names

Using tuples as customer-class names in Ciw queueing networks.

Ciw lets you name customer classes with anything orderable, and tuples are a
natural choice because they are immutable and can carry several attributes at
once. This package demonstrates the three cases from the post: tuples that work
(`("Baby", 0)`), tuples that fail because they mix types (`("Baby", 0)` beside
`(1,)`), and the fix of padding every tuple to the same length and types.

This package is the code from the blog post
[Can Ciw Use Tuples For Class IDs?](https://galenseilis.github.io/blog/posts/ciw-tuple-class-names/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-tuple-class-names"
```

Requires Python 3.11 or newer, and depends on `ciw`.

## Quick start

```python
from ciw_tuple_class_names import tuple_keys

simulation = tuple_keys.run_simulation(max_time=9)
len(simulation.get_all_records()) > 0
```

Run the console script to exercise all three cases:

```bash
ciw-tuple-class-names
```

It runs the two working networks and then prints the `TypeError` raised by the
mixed-type network.

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
