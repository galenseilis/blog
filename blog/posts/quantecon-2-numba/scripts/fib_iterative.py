"""Time a plain-Python implementation of the Fibonacci sequence."""

import numpy as np
from timeit import timeit

def fib(n):
    '''
    Adjusted from:
    https://lectures.quantecon.org/py/numba.html
    https://en.wikipedia.org/wiki/Fibonacci_number
    https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    '''

    if n == 1:
        return np.ones(1)
    elif n > 1:
        x = np.empty(n)
        x[0] = 1
        x[1] = 1
        for i in range(2,n):
            x[i] =  x[i-1] + x[i-2]
        return x
    else:
        print('WARNING: Check validity of input.')

print(timeit('fib(10)', globals={'fib':fib}))
