import numpy as np

from Game.main import Game
from NeuroEvolution.Population import Population

N_BIRDS = 200
MUTATION_RATE = 0.10

pop = Population(N_BIRDS, MUTATION_RATE)
game = Game(pop, n_birds=N_BIRDS)
game.run()

