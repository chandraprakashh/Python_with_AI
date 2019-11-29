#TSP Problem in Python
#Traveling Salesman Problem using mlrose library

import mlrose

# Create list of distances between pairs of cities

dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), (0, 5, 5.3852), \

             (0, 6, 4.0000), (0, 7, 2.2361), (1, 2, 1.0000), (1, 3, 2.8284), (1, 4, 2.0000), \

             (1, 5, 4.1231), (1, 6, 4.2426), (1, 7, 2.2361), (2, 3, 2.2361), (2, 4, 2.2361), \

             (2, 5, 4.4721), (2, 6, 5.0000), (2, 7, 3.1623), (3, 4, 2.0000), (3, 5, 3.6056), \

             (3, 6, 5.0990), (3, 7, 4.1231), (4, 5, 2.2361), (4, 6, 3.1623), (4, 7, 2.2361), \

             (5, 6, 2.2361), (5, 7, 3.1623), (6, 7, 2.2361)]

 

# Initialize fitness function object using dist_list

fitness_dists = mlrose.TravellingSales(distances = dist_list)

 

# Define optimization problem object

problem_fit2 = mlrose.TSPOpt(length = 8, fitness_fn = fitness_dists, maximize = False)

 

# Solve using genetic algorithm

best_state, best_fitness = mlrose.genetic_alg(problem_fit2, mutation_prob = 0.2, max_attempts = 100,

                                              random_state = 2)

print(best_fitness)