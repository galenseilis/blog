# notes-process-modelling

A labelled transition system (LTS) and its synchronous product, from notes on
the BPMAG process-modelling lectures.

A labelled transition system is a set of states together with a set of labelled
transitions between them. The synchronous product couples two systems so that
they must take a shared action together, which is the building block for
modelling a complex process out of smaller ones. This package contains the
`LTS` class, whose overloaded `*` operator computes that product, and the
two-machine worked example from the post.

This package is the code from the blog post
[Notes On BPMAG's Process Modelling Lectures](https://galenseilis.github.io/blog/posts/notes-process-modelling/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-process-modelling"
```

Requires Python 3.11 or newer. The package has no third-party dependencies.

## Quick start

```python
from notes_process_modelling import LTS

lts1 = LTS(
    ["s1", "s2"],
    ["a", "b"],
    {"s1": {"a": "s2", "b": "s1"}, "s2": {"a": "s1", "b": "s2"}},
    "s1",
    ["s2"],
)
lts2 = LTS(
    ["s3", "s4"],
    ["a", "c"],
    {"s3": {"a": "s4", "c": "s3"}, "s4": {"a": "s3", "c": "s4"}},
    "s3",
    ["s4"],
)

product = lts1 * lts2
product.A                  # {'a'}, the shared actions
product.initial_state      # 's1s3'
product.accepting_states   # ['s2s4']
```

Run the worked example with the console script:

```bash
notes-process-modelling
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
