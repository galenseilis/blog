# Tutorial

This tutorial builds the Bank Renege model, runs one simulation, and then
estimates the run-time distribution.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-simpy-bank-renege"
```

## 2. Run one simulation

```python
from ciw_simpy_bank_renege import network

simulation = network.run_simulation()
exit_times = [record.exit_date for record in simulation.get_all_records()]
print(max(exit_times))
```

The simulation stops once five customers have finished (served or reneged), so
the last exit time is the sojourn time for all five.

## 3. Look at the bounded-arrival distribution

The arrival stream is an exponential distribution wrapped so that no more than
five customers ever arrive:

```python
from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist
import ciw

dist = MaxArrivalDist(ciw.dists.Exponential(1 / 10), max_arrivals=5)
[dist.sample() for _ in range(6)]
```

The sixth sample is `inf`, so arrivals stop.

## 4. Estimate the run-time distribution

```python
from ciw_simpy_bank_renege import runtime

x = runtime.sample_run_times(n=1000)
params = runtime.fit_gamma(x)
print("Gamma shape, loc, scale:", params)
```

## 5. Plot the fit

```python
runtime.plot_run_times(x, output="run-times.png")
```

This histograms the run times and overlays the fitted Gamma density. The
console script does the full experiment (one million simulations) and writes
`figures/bank-renege-run-times.png`:

```bash
ciw-simpy-bank-renege
```

You now know the whole workflow. Next, read the
[how-to guides](how-to-guides.md) to vary the model.
