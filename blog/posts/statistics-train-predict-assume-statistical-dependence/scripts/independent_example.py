"""Example showing conditional means under independence."""

import numpy as np

x = np.random.randint(0, 2, size=10**4)
y = np.random.randint(0, 2, size=10**4)

print(np.mean(y[x == 0]), np.mean(y[x == 1]), np.mean(y))
