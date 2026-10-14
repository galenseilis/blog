'''
This script constructs the expression tree for a multiple linear
regression as shown earlier in this post.
'''
import os

import numpy as np
import sympy as sp
from graphviz import Source

vec_beta = np.array([sp.Symbol(f'\\beta_{i}') for i in range(3)])

vec_var = np.array([1, sp.Symbol('X'), sp.Symbol('Z')])

f = vec_beta @ vec_var + sp.Symbol('\\epsilon')

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)

Source(sp.dotprint(f)).render(
    filename=os.path.join(figures_dir, "expression_tree"),
    format="png",
    cleanup=True,
)
