import numpy as np

from parity_decomposition_in_python.parity import even_part, odd_part, parity_decomposition_vector


def test_even_odd_properties():
    t = np.array([-1.0, 0.0, 1.0, 2.0])
    f = lambda x: x ** 2 + 3 * x + 1  # neither even nor odd
    e, o = parity_decomposition_vector(f, t)
    # check reconstruction
    np.testing.assert_allclose(e + o, f(t), atol=1e-10)


def test_even_function():
    t = np.linspace(-2, 2, 50)
    f = lambda x: x ** 2
    e, o = parity_decomposition_vector(f, t)
    np.testing.assert_allclose(o, np.zeros_like(t), atol=1e-10)


def test_odd_function():
    t = np.linspace(-2, 2, 50)
    f = lambda x: x ** 3
    e, o = parity_decomposition_vector(f, t)
    np.testing.assert_allclose(e, np.zeros_like(t), atol=1e-10)
