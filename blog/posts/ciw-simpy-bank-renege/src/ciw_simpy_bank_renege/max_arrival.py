"""A distribution that stops arrivals after a fixed count.

An M/M/1 queue normally has an unlimited stream of arrivals. The Bank Renege
example instead fixes the total number of customers at five. This distribution
wraps an ordinary inter-arrival distribution and returns a sample from it for
the first ``max_arrivals`` calls, then returns positive infinity so that no
further arrivals ever occur.
"""

from __future__ import annotations

from typing import Optional

import ciw


class MaxArrivalDist(ciw.dists.Distribution):
    """Limit the number of arrivals from an underlying distribution.

    Attributes
    ----------
    dist:
        The underlying distribution used for sampling.
    max_arrivals:
        The maximum number of arrivals allowed.
    arrival_count:
        The current count of arrivals.
    """

    def __init__(self, dist: ciw.dists.Distribution, max_arrivals: int = 5) -> None:
        """Initialise the distribution.

        Parameters
        ----------
        dist:
            The underlying distribution to sample from.
        max_arrivals:
            The maximum number of arrivals allowed. Defaults to 5.
        """
        self.dist = dist
        self.max_arrivals = max_arrivals
        self.arrival_count = 0

    def sample(
        self, t: Optional[float] = None, ind: Optional[ciw.Individual] = None
    ) -> float:
        """Sample from the underlying distribution, up to ``max_arrivals``.

        Parameters
        ----------
        t:
            Optional time parameter.
        ind:
            Optional individual parameter representing the arrival.

        Returns
        -------
        float
            A sample from the underlying distribution, or positive infinity
            once the maximum number of arrivals has been reached.
        """
        if self.arrival_count < self.max_arrivals:
            self.arrival_count += 1
            return self.dist.sample()
        return float("inf")
