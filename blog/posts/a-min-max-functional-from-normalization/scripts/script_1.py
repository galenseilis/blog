from itertools import product

import sympy as sp
import pandas as pd

x = sp.Symbol('x')
b = sp.Symbol('b')
a = sp.Symbol('a')
F = sp.Function('F')
F_x = F(x)
F_b = F(b)
F_a = F(a)

ops = {
    
    'add' : lambda x,y: x + y,
    'subtract': lambda x,y: x - y,
    'mult' : lambda x,y: x * y,
    'divide': lambda x,y: x / y,
    'exp': lambda x,y: x ** y,
    'log': lambda x,y: sp.log(y, x)
    }

results = []
for f,g in product(ops, ops):
    result = ops[g](ops[f](F_x, F_a), ops[f](F_b, F_a))
    result = result.simplify()
    results.append([f, g, f'${sp.latex(result)}$'])

df = pd.DataFrame(results, columns=['f', 'g', 'Functional'])
print(df.to_markdown(index=False))
