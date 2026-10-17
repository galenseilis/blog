import numpy as np
import pytest

from ciw_simpy_bank_renege import network, runtime
from ciw_simpy_bank_renege.max_arrival import MaxArrivalDist


class CountingDist:
    """A trivial deterministic distribution for testing the counter."""

    def __init__(self, value=1.0):
        self.value = value
        self.calls = 0

    def sample(self, t=None, ind=None):
        self.calls += 1
        return self.value


def test_max_arrival_dist_returns_inf_after_limit():
    underlying = CountingDist(2.5)
    dist = MaxArrivalDist(underlying, max_arrivals=3)
    samples = [dist.sample() for _ in range(5)]
    assert samples[:3] == [2.5, 2.5, 2.5]
    assert samples[3:] == [float("inf"), float("inf")]
    assert dist.arrival_count == 3


def test_max_arrival_dist_defaults_to_five():
    dist = MaxArrivalDist(CountingDist())
    assert dist.max_arrivals == 5


def test_build_network_has_one_node():
    net = network.build_network()
    assert net is not None


def test_simulation_finishes_five_customers():
    simulation = network.run_simulation()
    records = simulation.get_all_records()
    assert len(records) == 5
    assert all(np.isfinite(record.exit_date) for record in records)


def test_run_time_is_positive():
    ciw = pytest.importorskip("ciw")
    ciw.seed(2018)
    net = network.build_network()
    assert runtime.run_time(net) > 0


def test_sample_run_times_count_and_positive():
    x = runtime.sample_run_times(n=5)
    assert len(x) == 5
    assert (x > 0).all()


def test_sample_run_times_is_reproducible():
    first = runtime.sample_run_times(n=5, random_seed=42)
    second = runtime.sample_run_times(n=5, random_seed=42)
    assert np.array_equal(first, second)


def test_fit_gamma_returns_three_parameters():
    params = runtime.fit_gamma(runtime.sample_run_times(n=20))
    assert len(params) == 3
    assert params[0] > 0
    assert params[2] > 0


def test_plot_run_times_saves_a_file(tmp_path):
    x = runtime.sample_run_times(n=20)
    output = tmp_path / "run-times.png"
    params = runtime.plot_run_times(x, output=str(output))
    assert output.exists()
    assert output.stat().st_size > 0
    assert len(params) == 3
