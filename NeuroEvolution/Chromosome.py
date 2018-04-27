import numpy as np
import random as rnd
from .nn import NeuralNetwork

__all__ = [
    "Chromosome",
]

class Chromosome(object):
    def __init__(self, n_hidden_layers=1, n_nodes=[6], n_inputs=2, n_classes=2):
        self.genotype = NeuralNetwork(
            n_hidden_layers=n_hidden_layers,
            n_nodes=n_nodes,
            n_inputs=n_inputs,
            n_classes=n_classes
        )
        self.fitness = 0

    def crossover(self, partner):
        child = Chromosome()
        child.genotype.output_layer.weights = np.divide(
            np.add(self.genotype.output_layer.weights, partner.genotype.output_layer.weights),
            2
        )
        child.genotype.output_layer.bias = np.divide(
            np.add(self.genotype.output_layer.bias, partner.genotype.output_layer.bias),
            2
        )

        for i in range(self.genotype.n_hidden_layers):
            child.genotype.hidden_layers[i].weights = np.divide(
                np.add(self.genotype.hidden_layers[i].weights, partner.genotype.hidden_layers[i].weights),
                2
            )
            child.genotype.hidden_layers[i].bias = np.divide(
                np.add(self.genotype.hidden_layers[i].bias, partner.genotype.hidden_layers[i].bias),
                2
            )

        return child

    def mutate(self, proba):
        if proba * 100 > rnd.randint(0, 100):
            pass

    def calc_fitness(self, score, dist_from_start, dist_to_tube):
        self.fitness = score**2 + dist_from_start - dist_to_tube
