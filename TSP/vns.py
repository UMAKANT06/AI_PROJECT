import math
import random
import tsp_utils
import animated_visualizer

import matplotlib.pyplot as plt


class VariableNeighborhoodSearch:
    def __init__(self, coords, stopping_iter):

        self.coords = coords
        self.sample_size = len(coords)
        self.stopping_iter = stopping_iter
        self.iteration = 1

        self.dist_matrix = tsp_utils.vectorToDistMatrix(coords)
        self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]
        print('-------------using variable neighborhood search-----------------')
        print('Initial weight:', self.curr_weight)

    def weight(self, sol):
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def shake(self, solution, k):
        candidate = list(solution)
        for _ in range(k):
            i = random.randint(0, self.sample_size - 1)
            j = random.randint(0, self.sample_size - 1)
            candidate[i], candidate[j] = candidate[j], candidate[i]
        return candidate

    def local_search(self, solution):
        best_solution = list(solution)
        best_weight = self.weight(best_solution)
        improved = True

        while improved:
            improved = False
            for i in range(self.sample_size - 1):
                for j in range(i + 1, self.sample_size):
                    candidate = list(best_solution)
                    candidate[i], candidate[j] = candidate[j], candidate[i]
                    candidate_weight = self.weight(candidate)
                    if candidate_weight < best_weight:
                        best_solution = candidate
                        best_weight = candidate_weight
                        improved = True

        return best_solution

    def vns(self):
        while self.iteration < self.stopping_iter:
            k = 1
            while k <= self.sample_size:
                candidate = self.shake(self.curr_solution, k)
                candidate = self.local_search(candidate)
                candidate_weight = self.weight(candidate)

                if candidate_weight < self.curr_weight:
                    self.curr_solution = candidate
                    self.curr_weight = candidate_weight
                    if candidate_weight < self.min_weight:
                        self.min_weight = candidate_weight
                        self.best_solution = candidate

                k += 1
                self.iteration += 1
                self.weight_list.append(self.curr_weight)
                self.solution_history.append(self.curr_solution)

        print('Minimum weight:', self.min_weight)
        print('Improvement:',
              round((self.initial_weight - self.min_weight) / (self.initial_weight), 4) * 100, '%')

    def animateSolutions(self):
        animated_visualizer.animateTSP(self.solution_history, self.coords)

    def plotLearning(self):
        plt.plot([i for i in range(len(self.weight_list))], self.weight_list)
        line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        plt.legend([line_init, line_min], ['Initial weight', 'Optimized weight'])
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.show()



