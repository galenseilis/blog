"""Naively simulate autoregressive (AR) time series data."""

import numpy as np
from typing import List

def simulate_ar(
    intercept: float,
    coefs: List[float],
    noise: float = 0.3,
    warmup: int = 10,
    steps: int = 200,
    rng=None
    ) -> np.ndarray:
    """Simulates an autoregressive (AR) time series.

    Args:
        intercept (float): The intercept term of the AR process.
        coefs (List[float]): List of coefficients for the lagged terms.
        noise (float, optional): The standard deviation of the Gaussian noise. Default is 0.3.
        warmup (int, optional): Number of initial steps to discard to allow the process to stabilize. Default is 10.
        steps (int, optional): Number of steps to simulate after the warmup period. Default is 200.

    Returns:
        np.ndarray: Simulated AR time series data of length `steps`.
    """
    rng = np.random.default_rng() if rng is None else rng
    max_lag = len(coefs)
    draws = np.zeros(warmup + steps)
    draws[:max_lag] = intercept
    for step in range(max_lag, warmup + steps):
        draws[step] = intercept + rng.normal(0, noise)
        for lag, coef in enumerate(coefs, start=1):
            draws[step] += coef * draws[step - lag]
    return draws[warmup:]
