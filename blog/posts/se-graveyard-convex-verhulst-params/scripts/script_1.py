import numpy as np
from sympy import *

t, p0, k, r = Symbol('t'), Symbol('p0'), Symbol('k'), Symbol('r')

p = k / (1 + ((k-p0)/p0) * exp(-r*t))

H = np.zeros((3,3), dtype=object)
for i, xi in enumerate((p0, k, r)):
    for j, xj in enumerate((p0, k, r)):
        H[i,j] = diff(diff(p, xi), xj)
H = Matrix(H)
