"""Print a statistical summary of the benchmark results."""

import os

import pandas as pd

here = os.path.dirname(os.path.abspath(__file__))
post_dir = os.path.abspath(os.path.join(here, ".."))
csv_path = os.path.join(post_dir, "figures", "benchmark_results.csv")

results = pd.read_csv(csv_path)

print(results.describe().to_string())
