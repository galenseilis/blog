import simpy
from typing import Generator
from script_2 import Car


def driver(env: simpy.Environment, car: Car) -> Generator[simpy.events.Timeout, None, None]:
    """
    Simulates a driver interrupting the action of a car after a timeout.

    Parameters:
    - env (simpy.Environment): The simulation environment in which the driver operates.
    - car (Car): The car object representing the vehicle whose action will be interrupted.

    Yields:
    - simpy.events.Timeout: A simulation event representing the passage of time.

    Notes:
    This function yields a timeout event after 3 simulation time units, at which point
    it interrupts the action of the specified car using the `interrupt` method.

    Example:
    ```python
    import simpy

    class Car:
        def __init__(self):
            self.action = env.process(self.drive())

        def drive(self):
            while True:
                print("Car is moving.")
                yield env.timeout(1)

    env = simpy.Environment()
    car = Car()
    env.process(driver(env, car))
    env.run(until=10)
    ```
    """
    yield env.timeout(3)
    car.action.interrupt()
