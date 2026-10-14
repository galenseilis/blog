"""Draw box plots of X at each simulated timepoint."""

import os

import matplotlib.pyplot as plt
import seaborn as sns

from dynamics_data import simulate

df, all_df = simulate()

sns.boxplot(data=df, x='Time', y='X', hue='Time', dodge=False)
plt.tight_layout()

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "dynamics_boxplot.png"), dpi=300, bbox_inches="tight")
plt.close()
