from typing import NoReturn

import ciw


class IASDeterministic(ciw.dists.Distribution):
    """
    Represents an "instant at start" (IAS) deterministic distribution.

    This distribution generates values based on an initial value, and it can be limited
    to a specified number of samples to be initially generated.

    Parameters:
        value (float): The fixed value to be returned by the distribution.
        limit (int, optional): The maximum number of samples to be initially generated. Defaults to 1.

    Attributes:
        value (float): The fixed value to be returned by the distribution.
        count (int): The current count of samples generated.
        limit (int): The maximum number of samples to be initially generated.

    Methods:
        sample(t=None, ind=None):
            Generates a sample from the distribution.

    Example:
        >>> dist = IASDeterministic(value=3.14, limit=2)
        >>> dist.sample(0)
        0
        >>> dist.sample(0)
        0
        >>> dist.sample(0)
        3.14
    """

    def __init__(self, value: float, limit: float = 1) -> NoReturn:
        """
        Initializes the IASDeterministic distribution with the given parameters.

        Parameters:
            value (float): The fixed value to be returned by the distribution.
            limit (int, optional): The maximum number of samples to be initially generated. Defaults to 1.
        """
        self.value = value
        self.count = 0
        self.limit = limit

    def sample(self, t:float = None, ind: ciw.Individual = None) -> float:
        """
        Generates a sample from the distribution.

        Parameters:
            t (float, optional): Time parameter, not used in this distribution.
            ind (int, optional): Index parameter, not used in this distribution.

        Returns:
            float: The fixed value if conditions are met; otherwise, returns None.
        """
        if t  <= 0 and self.count < self.limit:
            self.count += 1
            return 0
        else:
            return self.value

    def __repr__(self):
        return f"IASDistribution(value={self.value}, limit={self.limit})"
