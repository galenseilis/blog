"""Estimate 99% confidence and prediction intervals for a standard normal at various sample sizes."""

import os

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main():
    # Parameters
    mu = 0  # mean of the normal distribution
    sigma = 1  # standard deviation of the normal distribution
    alpha = 0.01  # 99% confidence level
    z = stats.norm.ppf(1 - alpha / 2)  # z-score for 99% confidence level

    # Sample sizes to plot
    sample_sizes = np.arange(1, 101)

    # Confidence intervals (CI) for different sample sizes
    ci_upper = mu + z * sigma / np.sqrt(sample_sizes)
    ci_lower = mu - z * sigma / np.sqrt(sample_sizes)

    # Prediction intervals (PI)
    pi_upper = mu + z * sigma * np.sqrt(1 + 1 / sample_sizes)
    pi_lower = mu - z * sigma * np.sqrt(1 + 1 / sample_sizes)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sample_sizes, np.zeros_like(sample_sizes), "k-", label="Mean (0)", lw=1)

    # Prediction Interval
    plt.fill_between(sample_sizes, pi_lower, pi_upper, color="red", label="Estimated 99% Prediction Interval")

    # Confidence Interval
    plt.fill_between(sample_sizes, ci_lower, ci_upper, color="orange", label="Estimated 99% Confidence Interval")

    # Labels and Title
    plt.title("Estimated 99% Confidence and Prediction Intervals for a Standard Normal Distribution")
    plt.xlabel("Sample Size")
    plt.ylabel("Interval Bounds")
    plt.legend()

    # Show the plot
    plt.grid(True)

    here = os.path.dirname(os.path.abspath(__file__))
    figures_dir = os.path.join(here, os.pardir, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    plt.savefig(
        os.path.join(figures_dir, "confidence_vs_prediction_intervals.png"),
        dpi=300,
        bbox_inches="tight",
    )


if __name__ == "__main__":
    main()
