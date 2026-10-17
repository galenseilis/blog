# How-to guides

## Change the arrival and service rates

The rates live in `network.py` as `arrival_rate = 1/10` and
`service_rate = 1/12`. Edit them, or build a network by hand:

```python
import ciw
from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist

network = ciw.create_network(
    arrival_distributions=[MaxArrivalDist(ciw.dists.Exponential(1 / 5), 5)],
    service_distributions=[ciw.dists.Exponential(1 / 8)],
    number_of_servers=[1],
    reneging_time_distributions=[ciw.dists.Uniform(1, 3)],
)
```

## Change the number of customers

The batch limit is the second argument to `MaxArrivalDist` and also the
`simulate_until_max_customers` argument:

```python
import ciw
from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist

network = ciw.create_network(
    arrival_distributions=[MaxArrivalDist(ciw.dists.Exponential(1 / 10), 20)],
    service_distributions=[ciw.dists.Exponential(1 / 12)],
    number_of_servers=[1],
    reneging_time_distributions=[ciw.dists.Uniform(1, 3)],
)
simulation = ciw.Simulation(network)
simulation.simulate_until_max_customers(20, method="Finish")
```

## Change the reneging patience

Pass a different reneging distribution:

```python
reneging_time_distributions=[ciw.dists.Uniform(0.5, 1.5)]
```

## Run fewer simulations

`sample_run_times` defaults to one million, which is slow. Pass a smaller
count while exploring:

```python
from ciw_simpy_bank_renege import runtime

x = runtime.sample_run_times(n=100)
```

## Save the plot somewhere else

```python
runtime.plot_run_times(x, output="/tmp/run-times.png")
```

## Get a reproducible sample

```python
x = runtime.sample_run_times(n=100, random_seed=42)
```
