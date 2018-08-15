import numpy as np

from Game.main import Game
from NeuroEvolution.Population import Population

N_BIRDS = 15
MUTATION_RATE = 0.02
N_WINNERS = 2

pop = Population(N_BIRDS, MUTATION_RATE, n_winners=N_WINNERS)
game = Game(pop, n_birds=N_BIRDS)
game.run()
