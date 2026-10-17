import simpy
from typing import Generator
from .car import Car


def driver(env: simpy.Environment, car: Car) -> Generator[simpy.events.Timeout, None, None]:
    """
    Simulates a driver interrupting the action of a car after a timeout.

    Parameters:
    - env (simpy.Environment): The simulation environment in which the driver operates.
    - car (Car): The car object representing the vehicle whose action will be interrupted.

    Yields:
    - simpy.events.Timeout: A simulation event representing the passage of time.
    """
    yield env.timeout(3)
    car.action.interrupt()
