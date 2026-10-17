# API reference

## SimPy model

### `car_process_interaction_simpy_ciw.car.Car(env)`

A process-based model of an electric car. The constructor stores `env` and
starts `run` via `env.process`, exposing it as `self.action`.

### `Car.run()`

The main loop: print the parking time, charge for `5` units (catching
`simpy.Interrupt` to print the interruption message), print the driving time,
and drive for `2` units.

### `Car.charge(duration)`

Yield a timeout of `duration`.

### `car_process_interaction_simpy_ciw.car_simpy.driver(env, car)`

Yield a timeout of `3` units and then call `car.action.interrupt()`.

## Ciw model

### `car_process_interaction_simpy_ciw.ciw_example.StepDist(first_value, second_value, step_t)`

A `ciw.dists.Distribution` that returns `first_value` while `t <= step_t` and
`second_value` afterwards.

### `car_process_interaction_simpy_ciw.ciw_example.PrintDistWrapper(dist, message)`

Wrap a Ciw distribution and print either `message` with the current time, or the
interruption message when the individual is on node `2` at time `3`. `.sample`
delegates to the wrapped distribution.

### `car_process_interaction_simpy_ciw.ciw_example.build_network()`

Return the two-node `ciw.network.Network` used in the post.

### `car_process_interaction_simpy_ciw.ciw_example.run_simulation(max_time=15)`

Build the network, run `simulate_until_max_time(max_time)`, and return the
`ciw.Simulation`.

### `car_process_interaction_simpy_ciw.ciw_example.main()`

Console-script entry point. Calls `run_simulation()` with the default horizon.

## Console script

| Command | Effect |
| --- | --- |
| `car-process-interaction-simpy-ciw` | prints the car event log |
