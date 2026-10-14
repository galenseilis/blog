from script_1 import jump_spots
import ciw
serv_dists = [ciw.dists.Deterministic(0) if i in jump_spots else ciw.dists.Deterministic(1) for i in range(30)]
