from car_process_interaction_simpy_ciw import Car
import simpy


def test_car_initializes():
    env = simpy.Environment()
    car = Car(env)
    assert car.env is env
