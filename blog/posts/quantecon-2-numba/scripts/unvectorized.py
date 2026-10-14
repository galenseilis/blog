"""Time the unvectorized evaluation of a function over a meshgrid."""

import numpy as np
import quantecon as qe

def f(x, y):
    return np.exp(np.abs(x -y**3)) *  np.cos(x**2 + y**2)

# generate data
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

start = qe.util.tic()
f(x, y)
end = qe.util.toc()
