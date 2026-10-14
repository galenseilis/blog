"""Find a root of ``sin(x) * exp(-x)`` with Brent's method on [3, 4]."""

import numpy as np
from scipy.optimize import brentq

# Define a single-variable function to find solutions in
f = lambda x: np.sin(x) * np.exp(-x)
# try out the Brent's algorithm
print(brentq(f, 3, 4))
