"""Wrap the deterministic service distributions so that each sample is announced."""

import ciw

from print_dist_wrapper import PrintDistWrapper

service_dists = [
  PrintDistWrapper(
    ciw.dists.Deterministic(5),
    'Start parking at'),
  PrintDistWrapper(
    ciw.dists.Deterministic(2),
    'Start driving at')
    ]
