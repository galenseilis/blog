from kelly_networks_ciw import run_simulation


def test_run_simulation():
    simulation, records = run_simulation(horizon=9, seed=2018)
    assert len(records) > 0
    assert simulation is not None
