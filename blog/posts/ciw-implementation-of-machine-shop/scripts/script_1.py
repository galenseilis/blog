import ciw
import pandas as pd

class CiwMachineShop:
    """
    A class to simulate a machine shop using Ciw.

    This class models a machine shop with a set of machines that can break
    and be repaired. It simulates the production of parts over a specified
    simulation time.

    Parameters:
    - mfft (float): Mean time between machine failures (default 300.0).
    - repair_time (float): Time required to repair a machine (default 30.0).
    - job_duration (float): Default duration of a single job (default 30.0).
    - num_machines (int): Number of machines in the shop (default 10).

    Attributes:
    - mfft (float): Mean time between machine failures.
    - break_mean (float): Mean time between machine failures in rate form.
    - repair_time (float): Time required to repair a machine.
    - network (ciw.network.Network): Ciw network configuration for simulation.

    Methods:
    - run(sim_time=4*7*24*60):
        Simulate the machine shop and return parts produced.

        Args:
        - sim_time (int): Total simulation time in minutes (default 4 weeks).

        Returns:
        - pandas.Series: A Series containing the number of parts produced for each job.

    - sample_parts_made(uptime, part_mean=10.0, part_sigma=2.0):
        Simulate parts production over a given uptime using a normal distribution.

        Args:
        - uptime (float): The duration for which parts production is simulated.
        - part_mean (float): Mean time to produce a part (default 10.0).
        - part_sigma (float): Standard deviation of time to produce a part (default 2.0).

        Returns:
        - int: The number of parts produced during the specified uptime.
    """
    def __init__(self, mfft=300.0, repair_time=30.0, job_duration=30.0, num_machines=10):
        """
        Initialize the CiwMachineShop.

        Args:
        mfft (float): Mean time between machine failures (default 300.0).
        repair_time (float): Time required to repair a machine (default 30.0).
        job_duration (float): Default duration of a single job (default 30.0).
        num_machines (int): Number of machines in the shop (default 10).
        """
        self.mfft = mfft
        self.break_mean = 1 / mfft
        self.repair_time = repair_time

        self.network = ciw.create_network(
            arrival_distributions=[ciw.dists.Sequential([0, float("inf")]), None],
            service_distributions=[
                ciw.dists.Exponential(rate=self.break_mean),
                ciw.dists.Deterministic(value=repair_time),
            ],
            routing=[[0, 1], [1, 0]],
            batching_distributions=[ciw.dists.Deterministic(num_machines), None],
            number_of_servers=[float("inf"), 1],
        )

    def run(self, sim_time=4*7*24*60):
        """
        Run the machine shop simulation and return the parts produced.

        Args:
        sim_time (int): Total simulation time in minutes (default 4 weeks).

        Returns:
        pandas.Series: A Series containing the number of parts produced for each job.
        """
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

    def sample_parts_made(self, uptime, part_mean=10.0, part_sigma=2.0):
        """
        Simulate the production of parts over a given uptime.

        Args:
        uptime (float): The duration for which parts production is simulated.
        part_mean (float): Mean time to produce a part (default 10.0).
        part_sigma (float): Standard deviation of time to produce a part (default 2.0).

        Returns:
        int: The number of parts produced during the specified uptime.
        """
        count = 0
        parts_time = 0
        while True:
            parts_time += ciw.dists.Normal(part_mean, part_sigma).sample()
            if parts_time >= uptime:
                return count
            else:
                count += 1
