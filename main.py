import numpy as np

from flappybird import Game
from NeuroEvolution.nn import NeuralNetwork

neural_net = NeuralNetwork(n_hidden_layers=1, n_nodes=[6], n_inputs=2, n_classes=2)
