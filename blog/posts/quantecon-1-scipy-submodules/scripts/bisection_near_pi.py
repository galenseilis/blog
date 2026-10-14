"""Find a root of ``sin(x) * exp(-x)`` near pi with bisect on [3, 4]."""

import numpy as np
from scipy.optimize import bisect

# Define a single-variable function to find solutions in
f = lambda x: np.sin(x) * np.exp(-x)
print(bisect(f, 3, 4))
