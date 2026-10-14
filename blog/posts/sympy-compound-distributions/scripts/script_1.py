from sympy.stats.compound_rv import CompoundDistribution
from sympy.stats.crv_types import NormalDistribution
from sympy.stats import Exponential, Normal

X = Normal('X', 2, 4)
L = Exponential('L', 100)
N = NormalDistribution(X, L)
C = CompoundDistribution(N)
