# ciw-snakes-ladders

A discrete-event simulation generalization of Snakes and Ladders using Ciw.

The classic game of Snakes and Ladders is a Markov chain: a player's position
is the state, and the chance of the next position depends only on the current
one. This package models that chain as a Ciw queueing network, where tiles are
nodes, ordinary moves take one unit of time, snakes and ladders are instant
jumps, and all six players enter at the first tile.

This package is the code from the blog post
[A Discrete Event Simulation Generalization of Snakes and Ladders Using Ciw](https://galenseilis.github.io/blog/posts/ciw-snakes-ladders/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-snakes-ladders"
```

Requires Python 3.11 or newer, and depends on `ciw` and `pandas`.

## Quick start

```python
from ciw_snakes_ladders import simulate

simulation = simulate.run_simulation()
print(f"Player {simulate.winner(simulation)} is the winner!")
```

Run the console script to simulate the game and print the winner:

```bash
ciw-snakes-ladders
```

Which prints:

```text
Player 1 is the winner!
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## Note on the routing matrix

Ciw interprets any probability mass a routing row leaves unassigned as a
chance of leaving the system. Since a die roll near the end of the board can
overshoot the final square, the packaged board clamps overshooting rolls onto
the final square so that every ordinary row sums to one. Without this,
players could leave the board before reaching the end and "the winner" would
be ill defined. See `src/ciw_snakes_ladders/board.py` for details.

## License

Released for reuse with attribution to the original blog post.
