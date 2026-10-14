"""Simulate the three-variable dynamical system used in this post."""

import numpy as np
import pandas as pd
from scipy.integrate import odeint

# Dynamical system definition
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
t = np.arange(0.0, 0.5, 0.001)


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, beta * x * y * z


def assign_timepoint(t):
    if 0 <= t <= 0.1:
        return 1
    elif t <= 0.2:
        return 2
    elif t <= 0.3:
        return 3
    else:
        return 4


def simulate(seed=2018, n_paths=100):
    """Return the sampled paths and the mean path of the dynamical system."""
    rng = np.random.default_rng(seed)

    # Generate random paths at selected timepoints
    times = np.array((0.1, 0.2, 0.3)).reshape(-1, 1)
    data = {}
    for i in range(n_paths):
        state0 = rng.normal(1, 0.05, size=3)
        states = odeint(f, state0, t)
        select_states = states[(t == 0.1) | (t == 0.2) | (t == 0.3)]
        data[i] = np.concatenate((times, select_states), axis=1)

    data = np.concatenate(tuple(data.values()))
    df = pd.DataFrame(data, columns=['Time', 'X', 'Y', 'Z'])
    df['timepoint'] = df['Time'].apply(assign_timepoint)

    # Generate mean path at many timepoints
    states0 = (1,) * 3
    states = odeint(f, states0, t)
    all_data = np.concatenate((t.reshape(-1, 1), states), axis=1)
    all_df = pd.DataFrame(all_data, columns=['Time', 'X', 'Y', 'Z'])

    return df, all_df
