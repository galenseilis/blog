"""Scheduled changes implementation."""

from __future__ import annotations

from typing import Callable, Iterable, Tuple

import ciw

ScheduleItem = Tuple[float, Iterable[Callable[[ciw.Simulation], ciw.Simulation]]]


def scheduled_changes(sim: ciw.Simulation, sched: ScheduleItem) -> ciw.Simulation:
    """
    Apply scheduled changes to simulation.

    Parameters:
        sim: Ciw Simulation
        sched (tuple): tuple of times and functions
    """
    for event in sched:
        time_to, funcs = event
        sim.simulate_until_max_time(sim.current_time + time_to)
        for func in funcs:
            sim = func(sim)
    return sim
