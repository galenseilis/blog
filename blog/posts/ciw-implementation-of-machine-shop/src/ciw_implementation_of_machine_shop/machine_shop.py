"""Machine shop implementation."""

from __future__ import annotations

import ciw
import pandas as pd


class CiwMachineShop:
    """A class to simulate a machine shop using Ciw."""

    def __init__(
        self,
        mfft: float = 300.0,
        repair_time: float = 30.0,
        job_duration: float = 30.0,
        num_machines: int = 10,
    ) -> None:
        self.mfft = mfft
        self.break_mean = 1.0 / mfft
        self.repair_time = repair_time

        self.network = ciw.create_network(
            arrival_distributions=[ciw.dists.Sequential([0.0, float("inf")]), None],
            service_distributions=[
                ciw.dists.Exponential(rate=self.break_mean),
                ciw.dists.Deterministic(value=float(repair_time)),
            ],
            routing=[[0.0, 1.0], [1.0, 0.0]],
            batching_distributions=[ciw.dists.Deterministic(num_machines), None],
            number_of_servers=[float("inf"), 1],
        )

    def run(self, sim_time: float = 4 * 7 * 24 * 60) -> pd.Series:
        sim = ciw.Simulation(self.network)
        sim.simulate_until_max_time(sim_time)
        recs = sim.get_all_records()
        df = pd.DataFrame(recs)
        parts = (
            df[df["node"] == 1]
            .groupby(by="id_number")["service_time"]
            .sum()
            .apply(self.sample_parts_made)
        )
        return parts

    def sample_parts_made(
        self, uptime: float, part_mean: float = 10.0, part_sigma: float = 2.0
    ) -> int:
        count = 0
        parts_time = 0.0
        while True:
            parts_time += ciw.dists.Normal(part_mean, part_sigma).sample()
            if parts_time >= uptime:
                return count
            count += 1
