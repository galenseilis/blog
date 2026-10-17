import ciw

from ciw_hack_initialize_individuals import initialize_queue_individuals


def test_initialize_queue_individuals():
    N = ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
        service_distributions=[ciw.dists.Exponential(rate=0.1)],
        number_of_servers=[3],
    )
    Q = ciw.Simulation(N)
    initialize_queue_individuals(Q, 1, 5, with_simulation=True)
    assert len(Q.nodes[1].individuals[0]) == 5
