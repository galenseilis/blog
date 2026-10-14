from typing import Generator, NoReturn
from simpy import Environment, Process, Timeout, Interrupt

class Car(object):
    """A simulation of an electric car that alternates between parking and charging,
    and driving states within a simulation environment.

    Attributes:
        env (Environment): The simulation environment in which the car operates.
        action (Process): The simulation process representing the car's activity.

    Methods:
        __init__(self, env: Environment):
            Initializes a new instance of the Car class.

            Parameters:
                env (Environment): The simulation environment.

        run(self) -> Generator[None, None, None]:
            The main behavior loop of the car, alternating between parking and charging,
            and driving states.

        charge(self, duration: int) -> Generator[None, None, None]:
            Simulates the charging process of the car for a specified duration.

            Parameters:
                duration (int): The duration for which the car charges its battery.
    """

    def __init__(self, env: Environment) -> NoReturn:
        """
        Initializes a new instance of the Car class.

        Parameters:
            env (Environment): The simulation environment.
        """
        self.env: Environment = env
        self.action: Process = env.process(self.run())

    def run(self) -> Generator[Timeout, None, None]:
        """
        The main behavior loop of the car, alternating between parking and charging,
        and driving states.
        """
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration: float = 5

            try:
                yield self.env.process(self.charge(charge_duration))
            except Interrupt:
                print('Was interrupted. Hope, the battery is full enough ...')

            print('Start driving at %d' % self.env.now)
            trip_duration: float = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration: float) -> Generator[Timeout, None, None]:
        """
        Simulates the charging process of the car for a specified duration.

        Parameters:
            duration (float): The duration for which the car charges its battery.
        """
        yield self.env.timeout(duration)
