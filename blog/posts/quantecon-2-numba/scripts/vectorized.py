"""Time a Numba ``vectorize``d evaluation of a function over a meshgrid."""

from numba import vectorize
import numpy as np
import quantecon as qe

@vectorize
def f(x, y):
    return np.exp(np.abs(x -y**3)) *  np.cos(x**2 + y**2)

# generate data
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

f(x,y) # precompile

start = qe.util.tic()
f(x, y)
end = qe.util.toc()
