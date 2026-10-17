import numpy as np


class Simulation:
    def __init__(self):
        """
        Initialize the simulation with default parameters.
        """
        self.num_in_system: int = 0
        self.clock: float = 0.0
        self.t_arrival: float = self.generate_interarrival()
        self.t_depart: float = float("inf")
        self.num_arrivals: int = 0
        self.num_departs: int = 0
        self.total_wait: float = 0.0

    def advance_time(self) -> None:
        """
        Advance the simulation time to the next event (either arrival or departure).
        """
        t_event: float = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_in_system * (t_event - self.clock)
        self.clock = t_event

        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
        else:
            self.handle_departure_event()

    def handle_arrival_event(self) -> None:
        """
        Handle an arrival event in the simulation.
        """
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_departure_event(self) -> None:
        """
        Handle a departure event in the simulation.
        """
        self.num_in_system -= 1
        self.num_departs += 1
        if self.num_in_system > 0:
            self.t_depart = self.clock + self.generate_service()
        else:
            self.t_depart = float("inf")

    def generate_interarrival(self) -> float:
        """
        Generate the time until the next arrival event using an exponential distribution.
        """
        return np.random.exponential(1 / 3)

    def generate_service(self) -> float:
        """
        Generate the service time for an entity using an exponential distribution.
        """
        return np.random.exponential(1 / 4)
