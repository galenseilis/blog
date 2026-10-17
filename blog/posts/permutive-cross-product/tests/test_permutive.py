from permutive_cross_product.permutive import find_4perm_cross_products, find_permutive_cross_products


def test_find_permutive_cross_products_returns_list():
    result = find_permutive_cross_products(dim=3)
    assert isinstance(result, list)


def test_find_4perm_cross_products_returns_dataframe():
    df = find_4perm_cross_products(dim=3, max_results=3)
    assert list(df.columns) == [
        "P1",
        "P2",
        "P3",
        "P4",
        "cross",
        "cross_dot_a",
        "cross_dot_b",
    ]
    assert len(df) <= 3
