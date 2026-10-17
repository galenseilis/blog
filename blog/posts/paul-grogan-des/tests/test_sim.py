from paul_grogan_des import Simulation


def test_sim_init():
    s = Simulation()
    assert s.clock == 0.0
    assert s.num_in_system == 0
