from pandigital_factorial.pandigital import is_pandigital, search_pandigital_factorials_up_to


def test_is_pandigital_basic():
    # 1023456789 contains all digits 0-9
    assert is_pandigital(1023456789) is True


def test_is_pandigital_false():
    assert is_pandigital(12345) is False


def test_is_pandigital_ten_digits():
    assert is_pandigital(1234567890) is True


def test_search_small():
    results = search_pandigital_factorials_up_to(k=10, m=5)
    assert len(results) == 10
    # Each result has 3 elements
    assert all(len(r) == 3 for r in results)
