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
        for i in range(len(self.genotype.output_layer.weights)):
            for j in range(len(self.genotype.output_layer.weights[0])):
                if proba * 100 > rnd.randint(0, 100):
                    self.genotype.output_layer.weights[i][j] = rnd.random()

        for i in range(len(self.genotype.output_layer.bias)):
            if proba * 100 > rnd.randint(0, 100):
                self.genotype.output_layer.bias[i] = rnd.random()

        for k in range(self.genotype.n_hidden_layers):
            for i in range(len(self.genotype.hidden_layers[k].weights)):
                for j in range(len(self.genotype.hidden_layers[k].weights[0])):
                    if proba * 100 > rnd.randint(0, 100):
                        self.genotype.hidden_layers[k].weights[i][j] = rnd.random()

            for i in range(len(self.genotype.hidden_layers[k].bias)):
                if proba * 100 > rnd.randint(0, 100):
                    self.genotype.hidden_layers[k].bias[i] = rnd.random()

    def calc_fitness(self, travelled_dist, dist_to_gap):      
        self.fitness = travelled_dist - abs(dist_to_gap)
