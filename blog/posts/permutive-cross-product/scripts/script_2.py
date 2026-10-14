import itertools

import pandas as pd
import sympy as sp
from sympy import latex

dim = 3

a = sp.Matrix([sp.Symbol(f'a{i+1}') for i in range(dim)])
b = sp.Matrix([sp.Symbol(f'b{i+1}') for i in range(dim)])
zero_vec = sp.Matrix([[0]]*dim)

results = []

for perm1 in itertools.permutations(range(dim)):
    for perm2 in itertools.permutations(range(dim)):
        for perm3 in itertools.permutations(range(dim)):
            for perm4 in itertools.permutations(range(dim)):
                P1 = sp.eye(dim)[perm1,:]
                P2 = sp.eye(dim)[perm2,:]
                P3 = sp.eye(dim)[perm3,:]
                P4 = sp.eye(dim)[perm4,:]

                cross = (P1 * a).multiply_elementwise(P2 * b) -\
                        (P3 * a).multiply_elementwise(P4 * b)


                if cross.dot(a).simplify() == 0 and cross.dot(b).simplify() == 0 and cross != zero_vec:
                    results.append(
                        [
                            f'${latex(P1)}$',
                            f'${latex(P2)}$',
                            f'${latex(P3)}$',
                            f'${latex(P4)}$',
                            f'${latex(cross)}$',
                            f'${latex(cross.dot(a).simplify())}$',
                            f'${latex(cross.dot(b).simplify())}$'
                            ]
                        )

result_markdown = pd.DataFrame(
                              results,
                              columns=['P1', 'P2', 'P3', 'P4', 'cross', 'cross_dot_a', 'cross_dot_b']
                              ).to_markdown()

print(result_markdown)
