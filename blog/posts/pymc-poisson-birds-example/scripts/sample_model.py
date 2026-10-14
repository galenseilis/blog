"""Draw posterior samples from the flower-visits Poisson model."""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pymc as pm

from model import model

# Sample from the posterior
rng = np.random.default_rng(2018)

with model:
    trace = pm.sample(random_seed=rng)
