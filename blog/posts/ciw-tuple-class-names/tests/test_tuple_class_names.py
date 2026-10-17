import pytest

from ciw_tuple_class_names import empty_string, mixed_types, tuple_keys


def test_tuple_keys_network_builds():
    network = tuple_keys.build_network()
    assert network is not None


def test_tuple_keys_simulation_runs():
    simulation = tuple_keys.run_simulation(max_time=9)
    assert len(simulation.get_all_records()) > 0


def test_mixed_type_tuples_raise_type_error():
    with pytest.raises(TypeError, match="not supported between instances"):
        mixed_types.build_network()


def test_empty_string_padding_builds_and_runs():
    network = empty_string.build_network()
    assert network is not None
    simulation = empty_string.run_simulation(max_time=9)
    assert len(simulation.get_all_records()) > 0
