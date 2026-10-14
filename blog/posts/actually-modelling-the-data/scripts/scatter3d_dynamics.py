"""Draw a three-dimensional scatter plot of the simulated states."""

import os

import matplotlib.pyplot as plt

from dynamics_data import simulate

df, all_df = simulate()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for time, dfi in df.groupby('Time'):
    ax.scatter(*dfi[['X', 'Y', 'Z']].to_numpy().T, label=f'Time={time}')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.tight_layout()

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "dynamics_3D_scatter.png"), dpi=300, bbox_inches="tight")
plt.close()
