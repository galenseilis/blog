"""Format all ordered pairs of a five element set for use in LaTeX."""

from itertools import product

X = 'a', 'b', 'c', 'd', 'e'
XxX = ['('+', '.join(i) + ')' for i in product(X, X)]
XxX = sorted(XxX)
XxX = str(XxX).replace("'", "")
XxX = XxX.replace("[", "\\\\{")
XxX = XxX.replace("]", "\\\\}")
print(XxX)
