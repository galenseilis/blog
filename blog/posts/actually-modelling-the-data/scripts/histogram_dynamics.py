"""Plot histograms of X at the first two simulated timepoints."""

import os

import matplotlib.pyplot as plt

from dynamics_data import simulate

df, all_df = simulate()

df.query("`timepoint` in (1,2)").groupby(by='timepoint')['X'].hist()

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "dynamics_histogram.png"), dpi=300, bbox_inches="tight")
plt.close()
