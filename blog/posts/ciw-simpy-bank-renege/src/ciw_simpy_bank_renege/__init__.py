"""A Ciw implementation of SimPy's Bank Renege example.

The public modules are:

* :mod:`ciw_simpy_bank_renege.max_arrival` -- a distribution that stops
  arrivals after a fixed number of customers.
* :mod:`ciw_simpy_bank_renege.network` -- the Bank Renege network and its
  simulation.
* :mod:`ciw_simpy_bank_renege.runtime` -- sampling many run times and fitting a
  Gamma distribution.
"""

from __future__ import annotations

from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist
from ciw_simpy_bank_renege.network import build_network, run_simulation

__all__ = ["MaxArrivalDist", "build_network", "run_simulation"]

__version__ = "0.1.0"
