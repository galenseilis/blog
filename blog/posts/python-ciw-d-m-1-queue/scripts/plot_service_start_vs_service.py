"""Plot the service start times against the service times for the D/M/1 queue."""

import os

import matplotlib

matplotlib.use("Agg")

import pandas as pd

from simulate_queue import records

here = os.path.dirname(os.path.abspath(__file__))
figures = os.path.join(here, "..", "figures")
os.makedirs(figures, exist_ok=True)

records = pd.DataFrame(records)
ax = records.plot(x='service_start_date', y='service_time')
ax.figure.savefig(
    os.path.join(figures, "service_start_vs_service.png"),
    dpi=300,
    bbox_inches="tight",
)
