"""Taylor expand the DKWM sample-size bound about its optimal value of n."""

import sympy

n = sympy.Symbol('n', real=True, positive=True)
p = sympy.Symbol('p', real=True, positive=True)
k = sympy.Symbol('k', integer=True, positive=True)
epsilon = sympy.Symbol('\\epsilon', real=True, positive=True)

f = sympy.log(1 + n) - sympy.log(p / k) - 2 * epsilon ** 2 * n
print(f.series(n, 1 / (2 * epsilon ** 2) - 1, 3))
