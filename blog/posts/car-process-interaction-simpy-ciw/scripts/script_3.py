from typing import Callable, NoReturn

import ciw
import hciw
from hciw.waitlist import create_existing_customers_from_list
import pandas as pd


from typing import NoReturn
import ciw

class StepDist(ciw.dists.Distribution):
    """A custom distribution representing a step function with two values.

    This distribution returns the first value until a specified time, after which
    it switches to the second value.

    Attributes:
        first_value (float): The initial value of the step function.
        second_value (float): The value of the step function after the step time.
        step_t (float): The time at which the step occurs.

    Methods:
        __init__(self, first_value: float, second_value: float, step_t: float) -> NoReturn:
            Initializes a new instance of the StepDist class.

            Parameters:
                first_value (float): The initial value of the step function.
                second_value (float): The value of the step function after the step time.
                step_t (float): The time at which the step occurs.

        sample(self, t: float = None, ind: ciw.Individual = None) -> float:
            Samples the step function at a given time.

            Parameters:
                t (float, optional): The time at which to sample the step function.
                    Defaults to None.
                ind (ciw.Individual, optional): Not used in this distribution.
                    Defaults to None.

            Returns:
                float: The sampled value of the step function at the specified time.
    """

    def __init__(self, first_value: float, second_value: float, step_t: float) -> NoReturn:
        """
        Initializes a new instance of the StepDist class.

        Parameters:
            first_value (float): The initial value of the step function.
            second_value (float): The value of the step function after the step time.
            step_t (float): The time at which the step occurs.
        """
        super().__init__()
        self.first_value: float = first_value
        self.second_value: float = second_value
        self.step_t: float = step_t

    def sample(self, t: float = None, ind: ciw.Individual = None) -> float:
        """
        Samples the step function at a given time.

        Parameters:
            t (float, optional): The time at which to sample the step function.
                Defaults to None.
            ind (ciw.Individual, optional): Not used in this distribution.
                Defaults to None.

        Returns:
            float: The sampled value of the step function at the specified time.
        """
        if t is not None and t <= self.step_t:
            return self.first_value
        else:
            return self.second_value



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

    def __init__(self, dist: ciw.dists.Distribution, message) -> NoReturn:
        """
        Initialize the PrintDistWrapper instance.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying probability distribution to be wrapped.
        - message (str): A custom message to be printed before sampling.
        """
        super().__init__()
        self.dist = dist
        self.message = message
            
    def sample(self, t=None, ind=None):
        """
        Generate a sample from the underlying distribution, printing a custom message.

        Parameters:
        - t: Optional parameter (if applicable to the underlying distribution).
        - ind: Optional parameter (if applicable to the underlying distribution).

        Returns:
        - The sampled value from the underlying distribution.

        Note: This method overrides the sample method of ciw.dists.Distribution.
        """
        if ind.node == 2 and t == 3:
            if t == 3:
                print('Was interrupted. Hope, the battery is full enough ...')
        else:
                print(self.message, t)
            
        return self.dist.sample(t, ind)
        




arrival_dists = [ciw.dists.Sequential([0, float('inf')]), None]
service_dists = [PrintDistWrapper(StepDist(3,5,3), 'Start parking at'), PrintDistWrapper(ciw.dists.Deterministic(2), 'Start driving at')]
num_servers = [1, 1]
R = [[0, 1], [1, 0]]

network = ciw.create_network(
    arrival_distributions = arrival_dists,
    service_distributions = service_dists,
    number_of_servers = num_servers,
    routing=R
    )

simulation = ciw.Simulation(network)

simulation.simulate_until_max_time(15)
