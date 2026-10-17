# Tutorial

This tutorial runs the Ciw version of the car example and explains the log it
prints.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/car-process-interaction-simpy-ciw"
```

## 2. Run the simulation

```bash
car-process-interaction-simpy-ciw
```

The output is:

```default
Start parking at 0
Was interrupted. Hope, the battery is full enough ...
Start parking at 5
Start driving at 10
Start parking at 12
```

## 3. What each line means

The car starts parking at time `0` and charges for `5` time units. A driver
process interrupts the car at time `3`, which prints the interruption message.
Parking resumes and reaches a stop at time `5`, and the next parking message is
printed after the drive from `5` to `10`. Driving then takes two units, ending
at `12`.

## 4. Run it from Python

```python
from car_process_interaction_simpy_ciw.ciw_example import run_simulation

simulation = run_simulation(max_time=15)
```

`run_simulation` prints as it runs and returns the completed `ciw.Simulation`
for inspection.

## 5. Try the SimPy model

```python
import simpy

from car_process_interaction_simpy_ciw import Car, driver

env = simpy.Environment()
car = Car(env)
env.process(driver(env, car))
env.run(until=15)
```

Continue with the [how-to guides](how-to-guides.md) to change the timings.
