"""Benchmark the simpy car example against its Rust implementation.

The simpy ``car.py`` example is run many times under CPython (and under PyPy
when it is installed) and the compiled Rust ``car`` executable is run the same
number of times. A normalized histogram of the run times is saved to
``figures/performance_histogram.png`` and the raw timings are saved to
``figures/benchmark_results.csv`` for summarization.
"""

import csv
import importlib.util
import os
import shutil
import subprocess
import sys
from time import perf_counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from run_python import run_python_file as py

here = os.path.dirname(os.path.abspath(__file__))
post_dir = os.path.abspath(os.path.join(here, ".."))
car_py = os.path.join(here, "car.py")
car_project = os.path.join(post_dir, "car")
car_exe = os.path.join(car_project, "target", "release", "car")

N = 100
BINS = 10


def time_python(interpreter):
    results = []
    for _ in range(N):
        tic = perf_counter()
        py(car_py, interpreter)
        toc = perf_counter()
        results.append(toc - tic)
    return results


def time_rust():
    subprocess.run(
        ["cargo", "build", "--release"],
        cwd=car_project,
        check=True,
        capture_output=True,
        text=True,
    )
    results = []
    for _ in range(N):
        tic = perf_counter()
        subprocess.run([car_exe], capture_output=True, text=True, check=True)
        toc = perf_counter()
        results.append(toc - tic)
    return results


if importlib.util.find_spec("simpy") is not None:
    cpython_results = time_python(sys.executable)
else:
    cpython_results = []
    print("simpy is not importable; skipping the CPython benchmark.")

if shutil.which("pypy3") is not None:
    pypy_results = time_python("pypy3")
else:
    pypy_results = []
    print("pypy3 was not found; skipping the PyPy benchmark.")

rust_results = time_rust()

os.makedirs(os.path.join(post_dir, "figures"), exist_ok=True)

for label, results in [
    ("CPython", cpython_results),
    ("PyPy", pypy_results),
    ("Rust", rust_results),
]:
    if not results:
        continue
    counts, bin_edges = np.histogram(results, bins=BINS)
    normalized_counts = counts / counts.sum()
    plt.bar(bin_edges[:-1], normalized_counts, width=np.diff(bin_edges), label=label)

plt.xscale("log")
plt.xlabel("Run Time, log(seconds)")
plt.ylabel("Relative Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(
    os.path.join(post_dir, "figures", "performance_histogram.png"),
    dpi=300,
    bbox_inches="tight",
)


def pad(results):
    return list(results) + [None] * (N - len(results))


with open(os.path.join(post_dir, "figures", "benchmark_results.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Rust", "CPython", "PyPy"])
    for rust, cpython, pypy in zip(
        pad(rust_results), pad(cpython_results), pad(pypy_results)
    ):
        writer.writerow([rust, cpython, pypy])
