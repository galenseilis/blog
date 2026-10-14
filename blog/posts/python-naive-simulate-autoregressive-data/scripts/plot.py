"""Plot the simulated autoregressive data and save the figure."""

import os
import sys

from matplotlib import pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulate import ar_data

fig, ax = plt.subplots(figsize=(8, 3))
ax.set_title("Generated Autoregressive Timeseries", fontsize=15)
ax.plot(ar_data)
ax.set_xlabel('Time')
ax.set_ylabel('Signal')

os.makedirs("figures", exist_ok=True)
fig.savefig("figures/autoregressive_timeseries.png", dpi=300, bbox_inches="tight")
plt.show()
