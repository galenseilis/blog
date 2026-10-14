from typing import NoReturn

import ciw


class PrintDistWrapper(ciw.dists.Distribution):
    """
    A wrapper class for a probability distribution that adds a print statement
    before sampling from the underlying distribution.

    Parameters:
    - dist (ciw.dists.Distribution): The underlying probability distribution to be wrapped.
    - message (str): A custom message to be printed before sampling.

    Note: This class inherits from ciw.dists.Distribution.

    Example:
    ```
    underlying_dist = SomeDistributionClass(parameters)
    wrapper_dist = PrintDistWrapper(underlying_dist, "Sampling from the distribution:")
    sample_result = wrapper_dist.sample()
    ```
    """

    def __init__(self, dist: ciw.dists.Distribution, message: str) -> NoReturn:
        """
        Initialize the PrintDistWrapper instance.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying probability distribution to be wrapped.
        - message (str): A custom message to be printed before sampling.
        """
        super().__init__()
        self.dist = dist
        self.message = message

    def sample(self, t: float = None, ind: ciw.Individual = None) -> float:
        """
        Generate a sample from the underlying distribution, printing a custom message.

        Parameters:
        - t: Optional parameter (if applicable to the underlying distribution).
        - ind: Optional parameter (if applicable to the underlying distribution).

        Returns:
        - The sampled value from the underlying distribution.

        Note: This method overrides the sample method of ciw.dists.Distribution.
        """
        print(self.message, t)
        return self.dist.sample(t, ind)
