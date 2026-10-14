"""Find a root of ``sin(x) * exp(-x)`` on the wide interval [-10, 10] with bisect."""

import numpy as np
from scipy.optimize import bisect

# Define a single-variable function to find solutions in
f = lambda x: np.sin(x) * np.exp(-x)
# try out the bisection algorithm
print(bisect(f, -10, 10))
