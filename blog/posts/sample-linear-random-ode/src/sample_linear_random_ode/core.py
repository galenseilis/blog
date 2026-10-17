import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from numpy.typing import NDArray


def linear_ode(y: NDArray[np.float64], t: float, A: NDArray[np.float64]) -> NDArray[np.float64]:
    """Computes the derivative of y at time t for a linear ODE system."""
    return A @ y


def sample_linear_random_ode(
    dim: int = 3,
    n_samples: int = 1000,
    t_max: int = 1000,
    n_points: int = 10000,
    seed: int = 2018,
    output_path: str = "2024-06-17-example-linear-random-ode.png",
    alpha: float = 0.01,
    style: str = "Solarize_Light2",
) -> str:
    """Sample from linear system of random ODEs and plot results."""
    rng = np.random.default_rng(seed)

    plt.style.use(style)

    fig, axes = plt.subplots(dim, 1, sharex=True)
    t = np.linspace(0, t_max, n_points)

    for i in range(n_samples):
        y0 = rng.uniform(-10, 110, size=dim)
        A = rng.uniform(-1, 1, size=(dim, dim)) / 500
        y = odeint(linear_ode, y0, t, args=(A,))

        for j in range(dim):
            axes[j].plot(t, y[:, j], alpha=alpha, color="k")

    for j in range(dim):
        axes[j].set_ylabel(f"X{j}")
        axes[j].grid(True)

    plt.xlabel("Time")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def main() -> None:
    sample_linear_random_ode()


if __name__ == "__main__":
    main()
