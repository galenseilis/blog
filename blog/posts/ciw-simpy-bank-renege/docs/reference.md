# API reference

## `ciw_simpy_bank_renege.max_arrival.MaxArrivalDist`

```python
MaxArrivalDist(dist, max_arrivals=5)
```

A Ciw distribution that samples from ``dist`` for the first ``max_arrivals``
calls and returns ``float('inf')`` thereafter.

| Attribute | Meaning |
| --- | --- |
| `dist` | The underlying distribution used for sampling. |
| `max_arrivals` | The maximum number of arrivals allowed. |
| `arrival_count` | The current count of arrivals. |

### `MaxArrivalDist.sample(t=None, ind=None) -> float`

Return a sample from `dist`, or `inf` once `max_arrivals` is reached.

## `ciw_simpy_bank_renege.network`

| Name | Description |
| --- | --- |
| `arrival_rate` | `1/10`. |
| `service_rate` | `1/12`. |
| `max_customers` | `5`. |
| `reneging_time` | `(1, 3)`. |
| `seed` | Default random seed, `2018`. |
| `build_network()` | Return the Bank Renege `ciw.network.Network`. |
| `run_simulation(random_seed=2018)` | Seed, build, run until five customers finish, and return the `ciw.Simulation`. |

## `ciw_simpy_bank_renege.runtime`

| Name | Description |
| --- | --- |
| `n_simulations` | Default number of simulations, `1_000_000`. |
| `output_path` | Default figure path, `figures/bank-renege-run-times.png`. |
| `run_time(network)` | Run one simulation from `network` and return the maximum exit time. |
| `sample_run_times(n=1000000, random_seed=2018)` | Return `n` simulated sojourn times as a NumPy array. |
| `fit_gamma(x)` | Fit a Gamma distribution to `x` and return `(shape, loc, scale)`. |
| `plot_run_times(x, output=..., bins=200)` | Histogram `x`, overlay the fitted density, save the figure, and return the parameters. |
| `main()` | Sample one million run times and save the fitted-density plot. |

## Console script

| Command | Effect |
| --- | --- |
| `ciw-simpy-bank-renege` | Runs one million simulations and writes `figures/bank-renege-run-times.png` |
