# Tutorial

This tutorial builds the Ciw network for a Snakes and Ladders board and
simulates it until a player reaches the final square.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-snakes-ladders"
```

## 2. Build the network

The network is assembled from five pieces: routing, arrivals, services,
batching, and servers.

```python
from ciw_snakes_ladders import simulate

network = simulate.build_network()
```

Each piece corresponds to a module:

- `board.build_routing_matrix()` returns the moves between tiles;
- `arrivals.build_arrival_distributions()` gives the one-off arrivals;
- `services.build_service_distributions()` gives the move times;
- `batching.build_batching_distributions()` gives the six-player batch;
- `servers.build_number_of_servers()` removes the per-tile concurrency limit.

## 3. Run the game

```python
simulation = simulate.run_simulation()
```

`run_simulation` seeds Ciw (default `2018`) and stops as soon as one player has
finished, that is, reached the end of the board.

## 4. Find the winner

```python
winner = simulate.winner(simulation)
print(f"Player {winner} is the winner!")
```

The output is `Player 1 is the winner!`. The console script does the same:

```bash
ciw-snakes-ladders
```

You now know the whole workflow. Next, read the
[how-to guides](how-to-guides.md) to vary the board and the seed.
