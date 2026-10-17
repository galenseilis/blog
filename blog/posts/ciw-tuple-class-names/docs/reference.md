# API reference

## `ciw_tuple_class_names.tuple_keys`

### `build_network() -> ciw.network.Network`

Return a three-node network with the tuple-named classes `("Baby", 0)` and
`("Child", 1)`.

### `run_simulation(max_time=9) -> ciw.Simulation`

Build the network, simulate it until `max_time`, and return the simulation.

### `main() -> None`

Run the simulation.

## `ciw_tuple_class_names.mixed_types`

### `build_network()`

Build the network whose classes are `("Baby", 0)` and `(1,)`. This never
returns: Ciw sorts the class names and raises `TypeError: '<' not supported
between instances of 'int' and 'str'`.

### `main() -> None`

Attempt the broken build and print the resulting `TypeError`.

## `ciw_tuple_class_names.empty_string`

### `build_network() -> ciw.network.Network`

Return the network with the empty-string-padded class names `("Baby", 0)` and
`("", 1)`.

### `run_simulation(max_time=9) -> ciw.Simulation`

Build and simulate the padded network.

### `main() -> None`

Run the padded simulation.

## `ciw_tuple_class_names.cli`

### `main() -> None`

Run both working networks, then demonstrate the mixed-type failure.

## Console script

| Command | Effect |
| --- | --- |
| `ciw-tuple-class-names` | Runs the working networks and reports the mixed-type `TypeError` |
