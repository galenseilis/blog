"""Arrival distributions for the car example: one car at ``t=0``, none thereafter."""

import ciw

arrival_dists = [ciw.dists.Sequential([0, float('inf')]), None]
