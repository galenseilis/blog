import ciw

from <local_script> import ops

schedule = ( # Ordered schedule of time-to-event and the functions to be applied to update the state of a simulation.
(10, (ops.func1, ops.func2)), 
(30, (ops.func1,)), 
(23, (ops.func1,))
)

def scheduled_changes(sim, sched):
	'''
	parameters:
		sim: Ciw Simulation
		sched (tuple): tuple of times and functions 
	'''
	for event in sched:
		time_to, funcs = event
		sim.simulate_until_max_time(sim.current_time + time_to)
		for func in funcs:
			sim = func(sim) # Transform the state of the simulation
	return sim
