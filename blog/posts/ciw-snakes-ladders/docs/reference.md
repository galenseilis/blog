# API reference

## `ciw_snakes_ladders.board`

| Name | Description |
| --- | --- |
| `jump_spots` | Tuple of tiles that are the heads of snakes or feet of ladders: `(7, 10, 14, 23, 24, 28)`. |
| `n_squares` | Number of tiles on the board, `30`. |
| `build_routing_matrix()` | Return the `30 x 30` routing matrix. Ordinary rows sum to one; the final tile is terminal. |

## `ciw_snakes_ladders.arrivals`

| Name | Description |
| --- | --- |
| `n_players` | Number of players, `6`. |
| `build_arrival_distributions()` | Return the per-tile arrival distributions: one arrival at time `0`, then `None`. |

## `ciw_snakes_ladders.services`

| Name | Description |
| --- | --- |
| `build_service_distributions()` | Return the per-tile service distributions: `Deterministic(0)` at jump spots, `Deterministic(1)` elsewhere. |

## `ciw_snakes_ladders.batching`

| Name | Description |
| --- | --- |
| `build_batching_distributions()` | Return the per-tile batch sizes: `Deterministic(n_players)` at the first tile, `None` elsewhere. |

## `ciw_snakes_ladders.servers`

| Name | Description |
| --- | --- |
| `build_number_of_servers()` | Return `float('inf')` for every tile. |

## `ciw_snakes_ladders.simulate`

| Name | Description |
| --- | --- |
| `seed` | Default random seed, `2018`. |
| `build_network()` | Assemble and return the `ciw.network.Network`. |
| `run_simulation(random_seed=2018)` | Seed Ciw, build the network, simulate until one player finishes, and return the `ciw.Simulation`. |
| `winner(simulation)` | Return the `id_number` of the player routed into the final square. |
| `main()` | Run the simulation and print `Player N is the winner!`. |

## Console script

| Command | Effect |
| --- | --- |
| `ciw-snakes-ladders` | Simulates a game and prints the winner |
