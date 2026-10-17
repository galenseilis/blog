from car_process_interaction_simpy_ciw import PrintDistWrapper, StepDist


def test_stepdist_samples():
    d = StepDist(3, 5, 3)
    assert d.sample(t=1) == 3
    assert d.sample(t=5) == 5


def test_print_wrapper_delegates():
    wrapper = PrintDistWrapper(StepDist(3, 5, 3), "Start parking at")
    assert wrapper.sample(t=1) == 3
