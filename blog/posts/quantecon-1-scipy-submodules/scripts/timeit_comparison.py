"""Compare the execution time of bisect, Newton-Raphson, and Brent's method."""

import numpy as np
from scipy.optimize import bisect, newton, brentq
from timeit import timeit

f = lambda x: np.sin(x) * np.exp(-x)

print(timeit(stmt='bisect(f, 3, 4)',\
    globals={'bisect':bisect, 'f':f},\
    number=100000) / 100000)
print(timeit(stmt='newton(f, np.pi / 4 + 1)',\
    globals={'newton':newton, 'f':f, 'np':np},\
    number=100000) / 100000)
print(timeit(stmt='brentq(f, 3, 4)',\
    globals={'brentq':brentq, 'f':f},\
    number=100000) / 100000)
