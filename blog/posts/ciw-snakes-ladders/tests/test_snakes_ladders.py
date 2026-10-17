import pandas as pd
import pytest

from ciw_snakes_ladders import simulate
from ciw_snakes_ladders.arrivals import build_arrival_distributions
from ciw_snakes_ladders.batching import build_batching_distributions
from ciw_snakes_ladders.board import (
    build_routing_matrix,
    jump_spots,
    n_squares,
)
from ciw_snakes_ladders.servers import build_number_of_servers
from ciw_snakes_ladders.services import build_service_distributions


def test_routing_matrix_is_square_and_correct_size():
    routing = build_routing_matrix()
    assert len(routing) == n_squares
    assert all(len(row) == n_squares for row in routing)


def test_ordinary_routing_rows_sum_to_one():
    routing = build_routing_matrix()
    for i, row in enumerate(routing):
        if i + 1 in jump_spots or i == n_squares - 1:
            continue
        assert sum(row) == pytest.approx(1.0)


def test_final_square_is_terminal():
    routing = build_routing_matrix()
    assert sum(routing[n_squares - 1]) == 0.0


def test_jump_spots_route_with_probability_one():
    routing = build_routing_matrix()
    for tile, target in [
        (10, 3),
        (7, 19),
        (14, 25),
        (24, 9),
        (23, 29),
        (28, 12),
    ]:
        assert routing[tile - 1][target - 1] == 1.0


def test_arrival_distributions_shape():
    arrivals = build_arrival_distributions()
    assert len(arrivals) == n_squares
    assert arrivals[1:] == (n_squares - 1) * [None]


def test_service_distributions_shape():
    services = build_service_distributions()
    assert len(services) == n_squares


def test_batching_distributions_shape():
    batching = build_batching_distributions()
    assert len(batching) == n_squares
    assert batching[1:] == (n_squares - 1) * [None]


def test_number_of_servers_is_unlimited():
    servers = build_number_of_servers()
    assert len(servers) == n_squares
    assert all(s == float("inf") for s in servers)


def test_simulation_produces_exactly_one_finisher():
    simulation = simulate.run_simulation()
    records = pd.DataFrame(simulation.get_all_records())
    exits = records[records.destination == -1]
    assert len(exits) == 1
    assert int(exits.id_number.iloc[0]) in range(1, 7)


def test_winner_reached_the_final_square():
    simulation = simulate.run_simulation()
    records = pd.DataFrame(simulation.get_all_records())
    final = records[records.node == n_squares]
    assert len(final) == 1
    assert simulate.winner(simulation) == int(final.id_number.iloc[0])


def test_main_prints_the_winner(capsys):
    simulate.main()
    captured = capsys.readouterr()
    assert captured.out.startswith("Player ")
    assert captured.out.strip().endswith("is the winner!")


def test_simulation_is_reproducible():
    first = simulate.winner(simulate.run_simulation())
    second = simulate.winner(simulate.run_simulation())
    assert first == second


