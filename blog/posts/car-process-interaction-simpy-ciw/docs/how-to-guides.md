# How-to guides

## Run for a different amount of simulated time

```python
from car_process_interaction_simpy_ciw.ciw_example import run_simulation

run_simulation(max_time=30)
```

## Change the charging and driving durations

`build_network` hard-codes a `StepDist(3, 5, 3)` (first value `3`, second value
`5`, step at `3`) and a `Deterministic(2)` drive. Copy `build_network` and edit
those numbers to change the schedule.

## Change the printed messages

`PrintDistWrapper` takes the message as its second argument. Change
`"Start parking at"` or `"Start driving at"` in `build_network`.

## Inspect the resulting records

`run_simulation` returns the `ciw.Simulation`, whose `nodes` hold the recorded
data frames.

```python
from car_process_interaction_simpy_ciw.ciw_example import run_simulation

simulation = run_simulation()
print(simulation.nodes[1].all_records)
```

## Switch to the SimPy implementation

For the process-interaction model use `Car` and `driver` directly.

```python
import simpy

from car_process_interaction_simpy_ciw import Car, driver

env = simpy.Environment()
car = Car(env)
env.process(driver(env, car))
env.run(until=15)
```
