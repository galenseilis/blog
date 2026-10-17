# How-to guides

## Change the arrival or service rate

`generate_interarrival` returns `np.random.exponential(1 / 3)` and
`generate_service` returns `np.random.exponential(1 / 4)`. Subclass `Simulation`
and override the two methods to change the rates.

```python
import numpy as np

from paul_grogan_des import Simulation


class Fast(Simulation):
    def generate_interarrival(self):
        return np.random.exponential(1 / 10)

    def generate_service(self):
        return np.random.exponential(1 / 12)


S = Fast()
for _ in range(2018):
    S.advance_time()
```

## Run for a fixed simulated time instead of a number of events

Keep stepping while the clock is below a horizon.

```python
from paul_grogan_des import Simulation

S = Simulation()
while S.clock < 2018:
    S.advance_time()
```

## Get reproducible results

Seed NumPy before creating the simulation.

```python
import numpy as np

from paul_grogan_des import Simulation

np.random.seed(2018)
S = Simulation()
for _ in range(2018):
    S.advance_time()
```

## Estimate the mean number in system

```python
from paul_grogan_des import Simulation

S = Simulation()
for _ in range(2018):
    S.advance_time()

print(S.total_wait / S.clock)
```

## Inspect the Ciw model

`paul_grogan_des.ciw_example` builds and runs the equivalent M/M/1 network. It
runs on import; seed it first for a reproducible run.

```python
import random

import numpy as np

import ciw

ciw.seed(2018)
from paul_grogan_des import ciw_example

print(ciw_example.sim.get_all_records())
```
