import random as rnd
from .Chromosome import Chromosome

__all__ = [
    "Population",
]

class Population(object):
    def __init__(self, popmax, mutation_rate):
        self.popmax = popmax
        self.mutation_rate = mutation_rate
        self.pop = []
        self.parents = [None, None]        
        self.generation = 0

    def init_population(self):
        for _ in range(self.popmax):
            self.pop.append(Chromosome())

    def calc_fitness(self):
        pass

    def selection(self):
        fitness_sum = 0
        for chromosome in self.pop:
            fitness_sum += int(chromosome.fitness)

        for j in range(2):
            k = rnd.randint(1, fitness_sum)
            i = 0
            while k > 0:
                k -= int(self.pop[i].fitness)
                i+=1

            i-=1
            self.parents[j] = self.pop[i]

    def generate(self):
        if self.generation > 0:
            self.selection()

            for i in range(self.popmax):
                child = self.parents[0].crossover(self.parents[1])
                child.mutate(self.mutation_rate)
                self.pop[i] = child

        else:
            self.init_population()
            
        self.generation += 1

    def status(self):
        if self.generation > 0:
            print("Generation", self.generation)
            for i in range(self.popmax):
                print(i, "th chromosome's fitness: ", self.pop[i].fitness)
            print("---------------------------")
            print()
