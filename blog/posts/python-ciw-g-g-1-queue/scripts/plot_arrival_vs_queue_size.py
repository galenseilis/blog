"""Plot the arrival dates against the queue length at arrival for the G/G/1 queue."""

import os

import matplotlib

matplotlib.use("Agg")

import pandas as pd

from simulate_queue import records

here = os.path.dirname(os.path.abspath(__file__))
figures = os.path.join(here, "..", "figures")
os.makedirs(figures, exist_ok=True)

records = pd.DataFrame(records)
ax = records.plot(x='arrival_date', y='queue_size_at_arrival')
ax.figure.savefig(
    os.path.join(figures, "arrival_vs_queue_size_at_arrival.png"),
    dpi=300,
    bbox_inches="tight",
)
