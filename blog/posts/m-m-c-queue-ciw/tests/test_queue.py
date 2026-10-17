from m_m_c_queue_ciw.queue import run_simulation


def test_m_m_c_runs():
    records = run_simulation(seed=123, horizon=10.0)
    assert isinstance(records, list)


def test_m_m_c_reproducible():
    records1 = run_simulation(seed=42, horizon=5.0)
    records2 = run_simulation(seed=42, horizon=5.0)
    assert records1 == records2
