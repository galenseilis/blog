import numpy as np
from sympy import *

sigma = Symbol("\\sigma", real=True)
rho = Symbol("\\rho", real=True)
beta = Symbol("\\beta", real=True)
t = Symbol("t", real=True)

x = Function("x")(t)
y = Function("y")(t)
z = Function("z")(t)

v = [sigma * (y - x), x * (rho - z - y), x * y - beta * z]

dvdt = [i.diff(t) for i in v]
agnesian1 = latex(np.prod(dvdt))

print(agnesian1)
