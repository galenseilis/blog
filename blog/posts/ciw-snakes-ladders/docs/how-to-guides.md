# How-to guides

## Run the game and print the winner

```bash
ciw-snakes-ladders
```

## Change the number of players

The batch size at the first tile controls how many players enter. Edit
`n_players` in `arrivals.py`, or build a custom batching list:

```python
import ciw
from ciw_snakes_ladders.batching import build_batching_distributions

batching = build_batching_distributions()
batching[0] = ciw.dists.Deterministic(10)
```

## Change the seed

```python
from ciw_snakes_ladders import simulate

simulation = simulate.run_simulation(random_seed=12345)
print(simulate.winner(simulation))
```

Different seeds can produce different winners, because events at the same time
are resolved randomly.

## Move the snakes and ladders

`board.jump_spots` lists the tiles that are jump spots, and the six explicit
entries in `build_routing_matrix` set their destinations:

```python
from ciw_snakes_ladders import board

board.jump_spots  # (7, 10, 14, 23, 24, 28)
```

Change both the tuple and the corresponding routing entry to move a jump.

## Inspect the raw records

```python
import pandas as pd
from ciw_snakes_ladders import simulate

simulation = simulate.run_simulation()
records = pd.DataFrame(simulation.get_all_records())
records[["id_number", "node", "arrival_date", "service_end_date", "destination"]]
```

A `destination` of `-1` marks a player leaving the board; a `destination` equal
to `30` marks the move into the final square.

## Check that a routing row is a valid distribution

Ciw treats unassigned probability as an exit. To confirm a row sums to one:

```python
from ciw_snakes_ladders.board import build_routing_matrix, n_squares

routing = build_routing_matrix()
sum(routing[0])  # 1.0 for an ordinary tile
sum(routing[n_squares - 1])  # 0.0, the final square is terminal
```
