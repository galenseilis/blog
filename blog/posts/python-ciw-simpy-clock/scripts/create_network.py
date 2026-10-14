"""Build the two-node Ciw network that models the pair of clocks."""

import ciw

from distributions import arrival_dists, service_dists
from number_of_tickers import number_of_tickers
from routing import routing

network = ciw.create_network(
    arrival_distributions = arrival_dists,
    service_distributions = service_dists,
    number_of_servers = number_of_tickers,
    routing = routing
    )
