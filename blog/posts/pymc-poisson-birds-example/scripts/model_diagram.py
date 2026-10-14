"""Render the flower-visits model as a Graphviz diagram and save it."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model import pm, model

os.makedirs("figures", exist_ok=True)
graph = pm.model_to_graphviz(model)
graph.render("figures/flower_visits_model", format="png", cleanup=True)
