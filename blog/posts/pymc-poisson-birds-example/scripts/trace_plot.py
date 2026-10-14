"""Plot the posterior distribution sampling trace and save the figure."""

import os
import sys

import matplotlib.pyplot as plt
import pymc as pm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sample_model import model, trace

# Inspect the trace
with model:
    pm.plot_trace(trace)

os.makedirs("figures", exist_ok=True)
plt.savefig("figures/flower_visits_trace.png", dpi=300, bbox_inches="tight")
