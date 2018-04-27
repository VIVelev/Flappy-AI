import numpy as np

from Game.main import Game
from NeuroEvolution.nn import NeuralNetwork

N_BIRDS = 10
NEURAL_NETS = [NeuralNetwork() for _ in range(N_BIRDS)]

game = Game(NEURAL_NETS)
game.run()

