import ciw
N = ciw.create_network(
    arrival_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=1.0),
                 None,
                 None],
        ('',1): [ciw.dists.Exponential(rate=2.0),
                  None,
                  None]
    },
    service_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=4.0),
                 ciw.dists.Exponential(rate=1.0),
                 ciw.dists.Deterministic(value=0.0)],
        ('',1): [ciw.dists.Exponential(rate=6.0),
                  ciw.dists.Deterministic(value=0.0),
                  ciw.dists.Exponential(rate=1.0)]
    },
    routing={('Baby',0): [[0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]],
             ('',1): [[0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]
    },
    number_of_servers=[1, 2, 3],
)

Q = ciw.Simulation(N)
Q.simulate_until_max_time(9)
