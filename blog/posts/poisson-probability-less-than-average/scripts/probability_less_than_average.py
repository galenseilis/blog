"""Plot the probability that a Poisson variable is at most its mean against the mean."""

import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson


def main():
    plt.plot([poisson(l).pmf(np.arange(0, l + 1)).sum() for l in range(1, 51)])
    plt.xlabel("$\\lambda$")
    plt.ylabel("$\\Pr [ X \\leq \\lambda ]$")

    here = os.path.dirname(os.path.abspath(__file__))
    figures_dir = os.path.join(here, os.pardir, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    plt.savefig(
        os.path.join(figures_dir, "probability_less_than_average.png"),
        dpi=300,
        bbox_inches="tight",
    )


if __name__ == "__main__":
    main()
