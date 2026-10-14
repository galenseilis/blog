'''
This script simulates a system of ordinary differential
equations and saves the results to a file.
'''
import os

import numpy as np
import pandas as pd
from scipy.integrate import odeint

post_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

# Dynamical system definition
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
t = np.arange(0.0, 0.5, 0.001)


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, beta * x * y * z

# Generate random paths at selected timepoints
times = np.array((0.1, 0.2, 0.3)).reshape(-1, 1)
data = {}
for i in range(100):
    print(i)
    state0 = np.random.normal(1, 0.05, size=3)

    states = odeint(f, state0, t)
    select_states = states[(t==0.1)|(t==0.2)|(t==0.3)]
    data[i] = np.concatenate((times, select_states), axis=1)


data = np.concatenate(tuple(data.values()))

df = pd.DataFrame(data, columns=['Time', 'X', 'Y', 'Z'])
df.to_csv(os.path.join(post_dir, 'select_dynamics_data.csv'), index=False)

# Generate mean path at many timepoints
states0 = (1,)*3
states = odeint(f, states0, t)

data = np.concatenate((t.reshape(-1,1), states), axis=1)
df = pd.DataFrame(data, columns=['Time', 'X', 'Y', 'Z'])
df.to_csv(os.path.join(post_dir, 'all_dynamics_data.csv'), index=False)
