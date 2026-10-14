import ciw
import pandas as pd

# Set a seed for repeatability
ciw.seed(2018)

# Specify where the jump spots are
jump_spots = (7,10,14,23,24,28)

# Construct routing matrix
R = [[0] * 30 for i in range(30)]

for i in range(30):
    if i+1 not in jump_spots:
        for j in range(i+1, min(i + 6, 29) + 1):
            R[i][j] = 1/6

R[10-1][3-1] = 1
R[7-1][19-1] = 1
R[14-1][25-1] = 1
R[24-1][9-1] = 1
R[23-1][29-1] = 1
R[28-1][12-1] = 1

# Assign distributions and number of servers
arr_dists = [ciw.dists.Sequential([0, float('inf')])] + 29 * [None]
serv_dists = [ciw.dists.Deterministic(0) if i in jump_spots else ciw.dists.Deterministic(1) for i in range(30)]
batch_dists = [ciw.dists.Deterministic(6)] + 29 * [None]
num_servers = [float('inf')] * 30

# Create network instance according to our specification
N = ciw.create_network(
    arrival_distributions=arr_dists,
    service_distributions=serv_dists,
    routing=R,
    batching_distributions=batch_dists,
    number_of_servers=num_servers
)

# Instantiate and run the simulation until someone wins (i.e. reaches the end)
Q = ciw.Simulation(N)
Q.simulate_until_max_customers(1, method='Finish')

# Extract and report winner from results
df = pd.DataFrame(
    Q.get_all_records()
    )

winner = df[df.destination == 30].id_number.to_numpy()[0]
print(f'Player {winner} is the winner!')
