from script_3 import nx
from script_3 import g
def caller(f):
    f()

for tgen in nx.topological_generations(g):
    for func in tgen:
        caller(func)
