## ClassDef SimulatedAnnealing

**SimulatedAnnealing**: The function of SimulatedAnnealing is an optimization algorithm that uses a combination of simulated annealing and iterative local search to find the minimum weight solution for the Traveling Salesman Problem (TSP).

**Attributes**:

* `coords`: a list of coordinates of all points in the TSP instance.
* `temp`: initial temperature parameter used in simulated annealing algorithm.
* `alpha`: cooling rate parameter used in simulated annealing algorithm.
* `stopping_temp`: stopping temperature parameter used in simulated annealing algorithm to determine when to stop iterating.
* `stopping_iter`: stopping iteration parameter used in simulated annealing algorithm to determine when to stop iterating.
* `iteration`: current iteration number of the algorithm.
* `dist_matrix`: a distance matrix of all points in the TSP instance.
* `curr_solution`: the current solution (a permutation of point indices) being optimized by the algorithm.
* `best_solution`: the best solution found so far, which is the minimum weight solution for the TSP instance.
* `solution_history`: a list containing all solutions found during the optimization process.
* `weight_list`: a list containing all weights of the solutions found during the optimization process.

**Code Description**: This class implements the simulated annealing algorithm to optimize the Traveling Salesman Problem (TSP) instance. The algorithm iteratively generates new candidate solutions by swapping adjacent points in the current solution, and evaluates their fitness using a nearest neighbor heuristic. The algorithm then determines whether to accept or reject the new candidate solution based on its weight and an acceptance probability determined by the temperature parameter. If accepted, the new solution becomes the current solution, and the algorithm updates the best solution if necessary. The algorithm iterates until a stopping criterion is met, such as reaching a maximum number of iterations or achieving a minimum weight solution.

The `animateSolutions` function creates an animation visualizing the optimization process by displaying the solution history for each iteration. The `plotLearning` function creates a line plot visualizing the learning curve of the algorithm, showing the evolution of the best solution's weight over time.

**Note**: This class is called from the `main` method in the TSP instance to perform optimization and create the animation and line plots. The output of this class is a minimum weight solution for the TSP instance.

**Output Example**: A possible appearance of the code's return value could be a list of coordinates representing the optimized tour (minimum weight solution) for the TSP instance, such as `[(x1, y1), (x2, y2), ..., (xn, yn)]`, where each coordinate is a point in the TSP instance. The output could also include an animation visualizing the optimization process and a line plot visualizing the learning curve of the algorithm.
### FunctionDef __init__(self, coords, temp, alpha, stopping_temp, stopping_iter)
**TSP/tsp_utils.py/distanceMatrixFunction**

The function of `distanceMatrixFunction` is to create a distance matrix from a coordinate list.

**parameters**:

* coords: A list of lists, where each inner list represents a 2D point and its corresponding distance with other points in the coordinate list.

**Code Description**: The function iterates through the input `coords` to calculate the Euclidean distance between all possible pairs of points. Then, it creates a square matrix where each element represents the distance between the corresponding points in the coordinate list.

This function is used by other classes in the project, such as the SimulatedAnnealing class and the VariableNeighborhoodSearch class, to calculate the initial solution for the simulated annealing algorithm and the variable neighborhood search algorithm, respectively. The nearest neighbor strategy uses this distance matrix to compute the initial solution.

The relationship between this function and its callers in the project can be seen as follows:

* In TSP/simulated_annealing.py, the SimulatedAnnealing class calls distanceMatrixFunction to create a distance matrix for simulated annealing algorithm.
* In TSP/vns.py, the VariableNeighborhoodSearch class also calls distanceMatrixFunction to create a distance matrix for variable neighborhood search algorithm.
* In TSP/nearest_neighbour.py, nearestNeighbourSolution function uses distanceMatrixFunction to compute the initial solution (nearest neighbor strategy) using the given distance matrix.

**Note**: This function uses the math library's sqrt() method to calculate the Euclidean distance between two points and the random module's randrange() method to select a random node from the coordinate list as the starting point for the tour. The nodes_to_visit list is used to keep track of the remaining nodes that have not been visited yet, and the nearest_node variable is used to store the current nearest neighbor of the previous node.

**Output Example**: A sample return value could be a square matrix where each element represents the distance between the corresponding points in the coordinate list. For example, if the input coordinate list was [[1, 2], [3, 4], [5, 6]], a possible return value could be [[0, 2, 4], [2, 0, 6], [4, 6, 0]].

==================


Please generate a detailed explanation document for this object based on the code of the target object itself .

Please write out the function of this Function in bold plain text, followed by a detailed analysis in plain text (including all details), in language English to serve as the documentation for this part of the code.

The standard format is as follows:

**__init__**: The function of __init__ is XXX. (Only code name and one sentence function description are required)
**parameters**: The parameters of this Function.
· parameter1: XXX
· parameter2: XXX
· ...
**Code Description**: The description of this Function.
(Detailed and CERTAIN code analysis and description...And please include the relationship with its callees in the project from a functional perspective.)
**Note**: Points to note about the use of the code

***
### FunctionDef weight(self, sol)

**weight**: The function of weight is to calculate the total distance between two cities in a TSP (Traveling Salesman Problem) instance using the provided dist_matrix.

**Parameters**: 

* self: An instance of the SimulatedAnnealing class.
* sol: A list representing the current solution, where each element is an index of a city in the TSP instance.

**Code Description**: The weight function takes a current solution (sol) and calculates its total distance using the dist_matrix provided during initialization of SimulatedAnnealing class. The formula used to calculate the distance between two cities is `sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])`. This function returns the total distance as a float value.

**Note**: The dist_matrix must be provided during initialization of SimulatedAnnealing class to calculate the weight of each solution.

**Output Example**: A possible return value of this function could be 15.0, which represents the total distance between the cities in a TSP instance where the first city is connected to the last city with a distance of 5 and all other cities are connected in a circular manner.
***
### FunctionDef acceptance_probability(self, candidate_weight)

**acceptance_probability**: The function of `acceptance_probability` is to calculate the acceptance probability for a given candidate solution based on the Simulated Annealing algorithm. It takes one parameter, `candidate_weight`, which represents the weight of the candidate solution, and returns a value between 0 and 1 that represents the probability of accepting the candidate solution.

**Parameters**:

* `candidate_weight`: The weight of the candidate solution to be evaluated.

**Code Description**: This function uses the absolute difference between the weight of the candidate solution and the current temperature (self.temp) to calculate the acceptance probability. It then applies the exponential function to this value to ensure that the probability decreases as the difference between the weights increases, providing a more balanced search space for the Simulated Annealing algorithm.

The relationship with its callers in the project is that it is used by the `SimulatedAnnealing` class to determine whether or not to accept a given candidate solution during the simulation. The class uses this function as part of its optimization process, and it is called repeatedly with different candidate solutions until an acceptable solution is found or the maximum number of iterations is reached.

**Note**: This function relies on the `self.temp` attribute being set to a value before calling it, as it uses this value to calculate the acceptance probability. It also assumes that the `candidate_weight` parameter is a valid weight value that can be used in mathematical operations with self.curr_weight.

**Output Example**: A possible output for this function might be 0.5 if the weight of the candidate solution is equal to half of the current temperature, and a probability of 0.9 if the weight is three times the current temperature. The exact value will depend on the specific values used as input.
***
### FunctionDef accept(self, candidate)

**accept**: The function of `accept` is to evaluate the weight of a candidate solution and determine whether or not to accept it based on the Simulated Annealing algorithm's acceptance probability.

**parameters**:

* `candidate_weight`: The weight of the candidate solution to be evaluated.

**Code Description**: This function takes a current solution (sol) and calculates its total distance using the dist_matrix provided during initialization of SimulatedAnnealing class. The formula used to calculate the distance between two cities is `sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])`. This function returns a value between 0 and 1 that represents the probability of accepting the candidate solution.

**Note**: The dist_matrix must be provided during initialization of SimulatedAnnealing class to calculate the weight of each solution. This function relies on the `self.temp` attribute being set to a value before calling it, as it uses this value to calculate the acceptance probability. It also assumes that the `candidate_weight` parameter is a valid weight value that can be used in mathematical operations with self.curr_weight.

**Output Example**: A possible output for this function might be 0.5 if the weight of the candidate solution is equal to half of the current temperature, and a probability of 0.9 if the weight is three times the current temperature. The exact value will depend on the specific values used as input.
***
### FunctionDef anneal(self)

**anneal**: The function of anneal is to perform simulated annealing on a given solution, which involves iteratively applying the temperature schedule and neighboring solutions accepted based on their weights.

**parameters**: 

* `self`: A reference to the current SimulatedAnnealing object.

**Code Description**: This function uses the Simulated Annealing algorithm's acceptance probability to determine whether or not to accept a given candidate solution as the next solution based on its weight. The temperature schedule is also applied to gradually reduce the current temperature over time, which allows for more diverse and exploratory solutions to be accepted. The function also keeps track of the minimum weight achieved so far and updates the current solution accordingly.

**Note**: This function relies on the `dist_matrix` attribute being set during initialization of SimulatedAnnealing class and assumes that the input candidate solution is a valid weight value that can be used in mathematical operations with self.curr_weight. The output example provided is just one possible outcome, and the exact value will depend on the specific values used as input.
***
### FunctionDef animateSolutions(self)

**animateSolutions**: The function of animateSolutions is to animate the solution over time.

**Parameters**:

* history: a list of solutions chosen by the algorithm
* points: an array_like of points with coordinates

**Code Description**: This code creates a plot of the TSP using Matplotlib and animates it over time. The key frames are calculated based on the length of the history list divided by 100, and the animation is initialized with the first frame. Each frame updates the solution on the graph by plotting a line through all the nodes in the history list.

This function is called by two other objects in the project: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions and TSP/vns.py/VariableNeighborhoodSearch/animateSolutions. Both of these functions are part of a larger algorithm for solving the Traveling Salesman Problem, and they use this function to visualize the solutions found by the algorithms.

**Note**: This code uses Matplotlib to create a plot of the TSP solution over time, which requires the matplotlib library to be installed. Additionally, this code assumes that the points are 2D coordinates stored in an array_like format.

**Output Example**: A possible appearance of the code's return value could be a visual representation of the Traveling Salesman Problem solution animated over time.
***
### FunctionDef plotLearning(self)

**plotLearning**: The function of plotLearning is to plot the learning process of the Simulated Annealing algorithm.

**parameters**:

* self (TSP): The instance of TSP class.

**Code Description**: This function uses the matplotlib library to plot the learning process of the Simulated Annealing algorithm. It first plots the weight list of the instance, then adds an initial weight line and a minimum weight line using the plt.axhline() method. Finally, it labels the y-axis as "Weight" and the x-axis as "Iteration". The plt.show() method is used to display the plot.

This function is called by the main function in TSP/tsp_sa.py/main, which is responsible for running the Simulated Annealing algorithm on a given instance of TSP. By calling this function, the user can visualize the learning process of the algorithm and observe its convergence to the minimum weight solution.

**Note**: This function requires the matplotlib library to be installed in order to work properly. It is recommended to use the latest version of matplotlib for best results.
***
