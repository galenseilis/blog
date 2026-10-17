from ciw_implementation_of_machine_shop import CiwMachineShop


def test_machine_shop_creation():
    ms = CiwMachineShop()
    assert ms is not None


def test_sample_parts_made():
    ms = CiwMachineShop()
    parts = ms.sample_parts_made(uptime=100, part_mean=10, part_sigma=2)
    assert isinstance(parts, int)
    assert parts >= 0
