from sympy import Integral
from sympy.stats.compound_rv import CompoundDistribution

from sympy_compound_distributions import compound_distribution


def test_compound_distribution_is_compound():
    c = compound_distribution()
    assert isinstance(c, CompoundDistribution)


def test_compound_distribution_repr():
    assert str(compound_distribution()) == "CompoundDistribution(NormalDistribution(X, L))"


def test_compound_pdf_is_an_integral():
    c = compound_distribution()
    pdf_at_zero = c.pdf(0)
    assert isinstance(pdf_at_zero, Integral)
