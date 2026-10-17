from bayesian_nn_cpd.model import build_model, simulate_data


def test_simulate_data_shape():
    observed, size = simulate_data(size=3)
    assert observed.size == size * size * size


def test_build_model_creates_model():
    observed, size = simulate_data(size=2)
    model = build_model(size=size, observed=observed)
    assert model is not None
