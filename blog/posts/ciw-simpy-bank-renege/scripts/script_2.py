from typing import Optional


import ciw
import numpy as np
from scipy.stats import gamma

ciw.seed(2018)
          
class MaxArrivalDist(ciw.dists.Distribution):
    """
    A custom distribution that limits the number of arrivals based on a maximum count.

    Attributes:
    - dist (ciw.dists.Distribution): The underlying distribution used for sampling.
    - max_arrivals (int): The maximum number of arrivals allowed.
    - arrival_count (int): The current count of arrivals.

    Methods:
    - sample(t: Optional[float] = None, ind: Optional[ciw.sampler.Individual] = None) -> float:
      Samples from the underlying distribution until the maximum number of arrivals is reached.
    """

    def __init__(self, dist: ciw.dists.Distribution, max_arrivals: int = 5):
        """
        Initializes the MaxArrivalDist.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying distribution to be used for sampling.
        - max_arrivals (int): The maximum number of arrivals allowed. Default is 5.
        """
        self.dist = dist
        self.max_arrivals = max_arrivals
        self.arrival_count = 0

    def sample(self, t: Optional[float] = None, ind: Optional[ciw.Individual] = None) -> float:
        """
        Samples from the underlying distribution until the maximum number of arrivals is reached.

        Parameters:
        - t (Optional[float]): Time parameter.
        - ind (Optional[ciw.sampler.Individual]): Individual parameter representing the arrival.

        Returns:
        - float: The sampled value from the distribution or positive infinity if the maximum arrivals limit is reached.
        """
        if self.arrival_count < self.max_arrivals:
            self.arrival_count += 1
            return self.dist.sample()
        return float('inf')


network = ciw.create_network(
    arrival_distributions=[MaxArrivalDist(ciw.dists.Exponential(1/10), 5)],
    service_distributions=[ciw.dists.Exponential(1/12)],
    number_of_servers=[1],
    reneging_time_distributions=[ciw.dists.Uniform(1,3)]
)

simulation = ciw.Simulation(network)
simulation.simulate_until_max_customers(5, method='Finish')
