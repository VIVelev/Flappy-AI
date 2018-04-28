import random as rnd
from .Chromosome import Chromosome

__all__ = [
    "Population",
]

class Population(object):
    def __init__(self, popmax, mutation_rate, n_winners=1):
        self.popmax = popmax
        self.mutation_rate = mutation_rate
        self.pop = []
        self.parents = [None, None]
        self.generation = 0
        self.n_winners = n_winners

    def init_population(self):
        for _ in range(self.popmax):
            self.pop.append(Chromosome())

    def calc_fitness(self):
        pass

    def parent_selection(self):
        # # # # # # # # # # # # # # # # # #
        # Fitness proportionate selection #
        # # # # # # # # # # # # # # # # # #
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
            new_pop = []

            # Add n winners directly (n=4)
            fitnesses = [chrom.fitness for chrom in self.pop]            
            for _ in range(self.n_winners):
                winner = fitnesses.index(max(fitnesses))
                fitnesses[winner] = -10**9 
                winner = self.pop[winner]
                winner.mutate(self.mutation_rate)
                new_pop.append(winner)                                               

            # # One child of the two best birds
            # child = new_pop[0].crossover(new_pop[1])
            # child.mutate(self.mutation_rate)
            # new_pop.append(child)

            # # Three children of random parents
            # for _ in range(3):
            #     partner_A = self.pop[rnd.randint(0, self.popmax-1)]
            #     partner_B = self.pop[rnd.randint(0, self.popmax-1)]
            #     child = partner_A.crossover(partner_B)
            #     child.mutate(self.mutation_rate)
            #     new_pop.append(child)

            # # Add two random birds
            # for _ in range(2):
            #     rnd_bird = self.pop[rnd.randint(0, self.popmax-1)]
            #     rnd_bird.mutate(self.mutation_rate)
            #     new_pop.append(rnd_bird)     
            
            for _ in range(self.popmax-self.n_winners):
                self.parent_selection()                
                child = self.parents[0].crossover(self.parents[1])
                child.mutate(self.mutation_rate)
                new_pop.append(child)

            self.pop = new_pop   

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
