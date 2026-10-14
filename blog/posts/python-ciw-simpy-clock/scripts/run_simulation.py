"""Instantiate the clock simulation and run it for two units of time."""

import ciw

from create_network import network

simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(2)
