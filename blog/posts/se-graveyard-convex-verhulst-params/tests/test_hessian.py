from se_graveyard_convex_verhulst_params import H


def test_hessian_shape():
    assert H.shape == (3, 3)


def test_hessian_symmetric():
    assert H == H.T
