import numpy as np

class Simulation:
    def __init__(self):
        """
        Initialize the simulation with default parameters.

        Attributes:
            num_in_system (int): The number of entities currently in the system.
            clock (float): The current simulation time.
            t_arrival (float): The time of the next arrival event.
            t_depart (float): The time of the next departure event.
            num_arrivals (int): The total number of arrivals that have occurred.
            num_departs (int): The total number of departures that have occurred.
            total_wait (float): The cumulative waiting time of all entities.
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

        This method updates the clock, total waiting time, and handles the next event.
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

        This method updates the number of entities in the system, schedules the next
        departure event if the system was previously empty, and schedules the next arrival event.
        """
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_departure_event(self) -> None:
        """
        Handle a departure event in the simulation.

        This method updates the number of entities in the system, schedules the next
        departure event if there are remaining entities, or sets the departure time to infinity if empty.
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

        Returns:
            float: The interarrival time.
        """
        return np.random.exponential(1 / 3)

    def generate_service(self) -> float:
        """
        Generate the service time for an entity using an exponential distribution.

        Returns:
            float: The service time.
        """
        return np.random.exponential(1 / 4)
