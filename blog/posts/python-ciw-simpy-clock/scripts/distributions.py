"""Arrival and service distributions for each clock's node."""

from clock_speeds import clock_speeds
from ias_deterministic import IASDeterministic

arrival_dists = [IASDeterministic(speed, 2) for speed in clock_speeds]
service_dists = [IASDeterministic(speed) for speed in clock_speeds]
