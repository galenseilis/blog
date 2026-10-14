"""Find a root of ``sin(x) * exp(-x)`` with Newton-Raphson from a low guess."""

import numpy as np
from scipy.optimize import newton

# Define a single-variable function to find solutions in
f = lambda x: np.sin(x) * np.exp(-x)
# try out the Newton-Raphson algorithm
print(newton(f, 0.2))
