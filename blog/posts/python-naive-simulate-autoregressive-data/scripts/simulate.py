"""Simulate the autoregressive process using the seeded generator and parameters."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulate_ar import simulate_ar
from seed import rng
from parameters import intercept, coefs

ar_data = simulate_ar(intercept, coefs, warmup=2018, steps=200, rng=rng)
