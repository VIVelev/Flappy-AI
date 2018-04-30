import numpy as np

from Game.main import Game
from NeuroEvolution.Population import Population

N_BIRDS = 5
MUTATION_RATE = 0.05
N_WINNERS = 1

pop = Population(N_BIRDS, MUTATION_RATE, n_winners=N_WINNERS)
game = Game(pop, n_birds=N_BIRDS)
game.run()
