from sympy.stats import *
import numpy as np
from sympy import latex, Symbol, Abs
from time import ctime

N = 101 

means = [Symbol(f'm{i}', real=True) for i in range(N)]
stds = [Symbol(f's{i}', real=True) for i in range(N)]
univars = [Normal(f'x{i}', means[i], stds[i]) for i in range(N)]

for i in range(2, N+1):
    print(ctime(), univars[:i])
    with open('equations.txt', 'a') as f:
        f.write(f'{ctime()} {univars[:i]}\n')
        select_vars = univars[:i]
        numerator = np.prod([v - E(v) for v in select_vars])
        denominator = np.prod([(Abs(v - E(v))**len(select_vars))**(1/len(select_vars)) for v in select_vars])
        f.write(latex(density(numerator / denominator)) + '\n\n')
