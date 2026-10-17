"""Parity decomposition of scalar functions."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def even_part(f: Callable[[np.ndarray], np.ndarray], t: np.ndarray) -> np.ndarray:
    """Compute the even part of a scalar function."""
    return 0.5 * (f(t) + f(-t))


def odd_part(f: Callable[[np.ndarray], np.ndarray], t: np.ndarray) -> np.ndarray:
    """Compute the odd part of a scalar function."""
    return 0.5 * (f(t) - f(-t))


def parity_decomposition_vector(
    f: Callable[[np.ndarray], np.ndarray], t: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return (even_part(t), odd_part(t)) for function f."""
    return even_part(f, t), odd_part(f, t)


def plot_parity_decomposition(
    f: Callable[[np.ndarray], np.ndarray],
    t: np.ndarray,
    output: str | Path = "example_parity_decomposition.png",
    dpi: int = 300,
    transparent: bool = True,
) -> Path:
    """Plot the parity decomposition and save to output."""
    e = even_part(f, t)
    o = odd_part(f, t)
    plt.plot(e, o)
    plt.xlabel("Even Part")
    plt.ylabel("Odd Part")
    out_path = Path(output)
    plt.savefig(out_path, dpi=dpi, transparent=transparent)
    plt.close()
    return out_path


def example_f(t: np.ndarray) -> np.ndarray:
    """Example function from the blog post."""
    return np.exp(np.cos(t) + np.sin(t))


def main() -> None:
    """Generate the example plot and reproduce original output."""
    t = np.linspace(-2 * np.pi, 2 * np.pi, num=1000)
    plot_parity_decomposition(example_f, t)


if __name__ == "__main__":
    main()
