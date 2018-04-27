from .Chromosome import Chromosome

__all__ = [
    "Population",
]

class Population(object):
    def __init__(self, popmax, mutation_rate):
        self.popmax = popmax
        self.mutation_rate = mutation_rate
        self.pop = []
        self.init_population()

    def init_population(self):
        for _ in range(self.popmax):
            self.pop.append(Chromosome())

    def calc_fitness(self):
        pass

    def selection(self):
        pass

    def generate(self):
        pass
