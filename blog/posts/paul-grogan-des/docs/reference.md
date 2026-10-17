# API reference

## `paul_grogan_des.simulation.Simulation()`

A hand-written event-advance simulation of a single-server (M/M/1) queue.

### Attributes

| Attribute | Meaning |
| --- | --- |
| `num_in_system` | entities currently in the system |
| `clock` | current simulation time |
| `t_arrival` | time of the next arrival |
| `t_depart` | time of the next departure (`inf` when idle) |
| `num_arrivals` | total arrivals handled |
| `num_departs` | total departures handled |
| `total_wait` | accumulated wait area, `sum(num_in_system * dt)` |

### `advance_time()`

Move the clock to `min(t_arrival, t_depart)`, add the elapsed area to
`total_wait`, and dispatch to `handle_arrival_event` or
`handle_departure_event`.

### `handle_arrival_event()`

Increment the population and arrival counter, schedule a departure if the system
was empty, and schedule the next arrival.

### `handle_departure_event()`

Decrement the population and increment the departure counter; schedule the next
departure or set `t_depart = inf` if the system is now empty.

### `generate_interarrival()`

Return `numpy.random.exponential(1 / 3)`.

### `generate_service()`

Return `numpy.random.exponential(1 / 4)`.

## `paul_grogan_des.run.main()`

Construct a `Simulation` and advance it `2018` times. Console-script entry point.

## `paul_grogan_des.ciw_example`

Module-level Ciw implementation of the same M/M/1 system with arrival rate `3`
and service rate `4`. Running (or importing) it seeds Ciw with `2018`, runs a
one-node network until time `2018`, and binds the result to `sim`.

## Console script

| Command | Effect |
| --- | --- |
| `paul-grogan-des` | advance the hand-written simulation 2018 times |
