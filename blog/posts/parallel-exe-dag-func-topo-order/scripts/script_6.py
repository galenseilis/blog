from script_3 import nx
from script_3 import g
from script_5 import caller
from multiprocessing import Pool

for tgen in nx.topological_generations(g):
    with Pool(processes=4) as pool:
        pool.map(caller, tgen)
