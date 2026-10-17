from m_d_c_queue_ciw import simulate


def test_run_simulation():
    simulation, records = simulate.run_simulation(horizon=10, seed=2018)
    assert len(records) > 0
    assert simulation is not None
