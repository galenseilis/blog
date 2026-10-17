from agnesian_lorenz_sympy_example.agnesian import agnesian_lorenz_order1


def test_agnesian_lorenz_order1_is_string():
    result = agnesian_lorenz_order1()
    assert isinstance(result, str)
    assert "\\sigma" in result
    assert "\\rho" in result
    assert "\\beta" in result
