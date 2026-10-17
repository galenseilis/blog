import numpy as np
from sympy import Matrix, diff, exp, symbols

t, p0, k, r = symbols("t p0 k r")


def verhulst(t, p0, k, r):
    return k / (1 + (k - p0) * exp(-r * t) / p0)


def hessian():
    p = verhulst(t, p0, k, r)
    H = np.zeros((3, 3), dtype=object)
    params = (p0, k, r)
    for i, pi in enumerate(params):
        for j, pj in enumerate(params):
            H[i, j] = diff(p, pi, pj)
    return Matrix(H)


H = hessian()
