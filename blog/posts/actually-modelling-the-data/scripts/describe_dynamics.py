"""Print summary statistics of the simulated dynamical system data."""

from dynamics_data import simulate

df, all_df = simulate()

print(df.describe())
