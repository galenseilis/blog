"""Deterministic service distributions for parking (5) and driving (2)."""

import ciw

service_dists = [ciw.dists.Deterministic(5), ciw.dists.Deterministic(2)]
