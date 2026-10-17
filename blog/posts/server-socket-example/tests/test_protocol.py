from server_socket_example.protocol import (
    deserialize,
    process_data,
    serialize,
)


def test_serialize_round_trip():
    data_structure = {"key": "value", "numbers": [1, 2, 3]}
    assert deserialize(serialize(data_structure)) == data_structure


def test_process_data_increments_numbers():
    received = {"key": "value", "numbers": [1, 2, 3]}
    assert process_data(received) == {"key": "processed", "numbers": [2, 3, 4]}


def test_process_data_leaves_input_unchanged():
    received = {"key": "value", "numbers": [1, 2, 3]}
    process_data(received)
    assert received == {"key": "value", "numbers": [1, 2, 3]}
