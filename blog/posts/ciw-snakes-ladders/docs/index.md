# ciw-snakes-ladders documentation

`ciw-snakes-ladders` is a discrete-event simulation of Snakes and Ladders built
with [Ciw](https://ciw.readthedocs.io/en/latest/). Each tile is a queueing
node, an ordinary move is a one-unit service, and a snake or ladder is an
instant jump.

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): build the network and simulate a game.
- [How-to guides](how-to-guides.md): change the number of players, the board,
  and the seed; read the records.
- [Reference](reference.md): the six modules and the console script.
- [Explanation](explanation.md): the board as a Markov chain, why Ciw differs
  from the original game, and why the routing rows must sum to one.
