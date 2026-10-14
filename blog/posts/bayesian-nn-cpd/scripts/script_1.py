'''Toy example of tensor decomposition in PyMC.

This example only performs a rank-1 decomposition.
'''

import pickle

import arviz as az
import numpy as np
import pymc as pm
from pytensor import tensor as at

# Prior Predictive Simulation
SIZE = 3

u1 = np.random.exponential(0.001, size=SIZE)
u2 = np.random.exponential(0.001, size=SIZE)
u3 = np.random.exponential(0.001, size=SIZE)
x = np.outer(u1, u2)
x = np.outer(x, u3).reshape((SIZE,) * 3).flatten()

# Model Specification
model = pm.Model()

with model:
    u1 = pm.Exponential("u1", lam=1, size=SIZE)
    u2 = pm.Exponential("u2", lam=1, size=SIZE)
    u3 = pm.Exponential("u3", lam=1, size=SIZE)
    mu = at.outer(at.outer(u1, u2), u3).flatten()

    X = pm.Exponential("X", mu, shape=SIZE * 3, observed=x)


if __name__ == "__main__":
    # Sample from the posterior distribution
    with model:
        idata = pm.sample(cores=12)

    # Save results for further analysis.
    with open("test.pickle", "wb") as handle:
        pickle.dump(idata, handle)
