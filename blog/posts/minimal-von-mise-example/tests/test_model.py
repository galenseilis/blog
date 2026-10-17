import numpy as np

from minimal_von_mise_example.model import build_model


def test_build_model_default():
    model = build_model()
    assert model is not None


def test_build_model_custom_observed():
    model = build_model(observed=np.array([0.1, 0.2, -0.1]))
    assert model is not None
