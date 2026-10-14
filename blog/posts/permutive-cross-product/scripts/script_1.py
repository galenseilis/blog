import itertools

import sympy as sp

dim = 3

a = sp.Matrix([sp.Symbol(f'a{i+1}') for i in range(dim)])
b = sp.Matrix([sp.Symbol(f'b{i+1}') for i in range(dim)])
zero_vec = sp.Matrix([[0]]*dim)

for perm in itertools.permutations(range(dim)):
    P = sp.eye(dim)[perm,:]

    cross = (P * a).multiply_elementwise(P.T * b) -\
            (P.T * a).multiply_elementwise(P * b)

    if cross.dot(a).simplify() == 0 and cross.dot(b).simplify() == 0 and cross != zero_vec:
        print(sp.latex(cross))
