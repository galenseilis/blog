"""Create the two-node Ciw network that models the parked/driving car."""

import ciw

from arrival_distributions import arrival_dists
from number_of_servers import num_servers
from routing_matrix import R
from wrapped_service_distributions import service_dists

network = ciw.create_network(
    arrival_distributions = arrival_dists,
    service_distributions = service_dists,
    number_of_servers = num_servers,
    routing=R
    )
