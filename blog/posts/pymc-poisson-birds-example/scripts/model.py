"""Define the PyMC Poisson model for the flower-visit counts."""

import os

import pymc as pm
import pandas as pd
import numpy as np

POST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(POST_DIR, 'flower_visits.csv'))

# Convert categorical columns to integer indices
df['Category_ID_code'] = pd.Categorical(df['Category_ID']).codes
df['Species_code'] = pd.Categorical(df['Species']).codes

# Coordinates for PyMC
coords = {
    'locations': df['Category_ID'].unique(),
    'species': df['Species'].unique()
}

with pm.Model() as model:
    # Define priors for λ
    num_categories = len(df['Category_ID'].unique())
    num_species = len(df['Species'].unique())
    λ = pm.Exponential('λ', 1.0, shape=(num_categories, num_species))

    # Define the observed data
    indices = (df['Category_ID_code'].values, df['Species_code'].values)
    observed_data = df['Total_visits'].values

    # Likelihood
    likelihood = pm.Poisson('flower_visits', mu=λ[indices], observed=observed_data)
