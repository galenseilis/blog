# car-process-interaction-simpy-ciw

Two implementations of the SimPy "car" example: the SimPy process-interaction
version and a Ciw discrete-event simulation that reproduces the same event log.

In the SimPy version a `Car` process alternates between parking/charging and
driving, and a `driver` process interrupts the car after three time units. The
Ciw version encodes the same behaviour as a two-node queueing network, using a
`StepDist` step function and a `PrintDistWrapper` to print the "Start parking
at", "Start driving at", and "Was interrupted" messages.

This package is the code from the blog post
[A Ciw Implementation of SimPy's Car Example With a Process Interaction](https://galenseilis.github.io/blog/posts/car-process-interaction-simpy-ciw/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/car-process-interaction-simpy-ciw"
```

Requires Python 3.11 or newer and depends on `simpy` and `ciw`.

## Quick start

```bash
car-process-interaction-simpy-ciw
```

prints the event log:

```default
Start parking at 0
Was interrupted. Hope, the battery is full enough ...
Start parking at 5
Start driving at 10
Start parking at 12
```

## Docs

Start at [`docs/index.md`](docs/index.md).
