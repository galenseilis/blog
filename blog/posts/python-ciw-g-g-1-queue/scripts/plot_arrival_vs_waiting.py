"""Plot the arrival times against the waiting times for the G/G/1 queue."""

import os

import matplotlib

matplotlib.use("Agg")

import pandas as pd

from simulate_queue import records

here = os.path.dirname(os.path.abspath(__file__))
figures = os.path.join(here, "..", "figures")
os.makedirs(figures, exist_ok=True)

records = pd.DataFrame(records)
ax = records.plot(x='arrival_date', y='waiting_time')
ax.figure.savefig(
    os.path.join(figures, "arrival_vs_waiting.png"),
    dpi=300,
    bbox_inches="tight",
)
