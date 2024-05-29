## ClassDef VariableNeighborhoodSearch

**VariableNeighborhoodSearch**: The VariableNeighborhoodSearch class is a TSP algorithm that uses a variable neighborhood search strategy to find the optimal solution for a given set of coordinates.

**Attributes**:

* `coords`: A list of coordinates in the form [(x1, y1), (x2, y2), ..., (xn, yn)]
* `stopping_iter`: The maximum number of iterations to perform
* `sample_size`: The size of the sample used for shaking
* `dist_matrix`: A distance matrix calculated from the coordinates
* `curr_solution`: The current solution being iterated on
* `best_solution`: The best solution found so far
* `initial_weight`: The initial weight of the problem
* `min_weight`: The minimum weight of the problem
* `weight_list`: A list of weights calculated during each iteration
* `solution_history`: A history of solutions generated during each iteration

**Code Description**:

The VariableNeighborhoodSearch class implements the variable neighborhood search algorithm for solving TSP problems. The algorithm iteratively shakes the current solution and calculates its weight using a local search method to find the optimal solution. The stopping criterion is based on the maximum number of iterations specified in `stopping_iter`.

The class constructor initializes the attributes and calculates the distance matrix from the coordinates provided. It also sets the initial solution, best solution, initial weight, minimum weight, and a list to store the weights calculated during each iteration.

The `vns` method performs the variable neighborhood search algorithm. It iteratively shakes the current solution using the `shake` method with a random sample size between 1 and `sample_size`, calculates the weight of the candidate solution using the `weight` method, and updates the best solution if the new weight is better than the previous one. The stopping criterion is based on the maximum number of iterations specified in `stopping_iter`.

The `plotLearning` method plots a graph of the weights calculated during each iteration against the iteration number. It also plots the initial weight and the optimized weight as horizontal lines.

**Note**: The VariableNeighborhoodSearch class relies on the `animateTSP` function provided by the `animated_visualizer` module to generate visualizations of the solutions.

**Output Example**: A mock output example showing the variable neighborhood search algorithm generating a solution for a TSP problem with 10 coordinates and iteratively shaking the current solution until reaching the optimal solution after 5 iterations:
```python
>>> vns = VariableNeighborhoodSearch(coords, stopping_iter=5)
>>> vns.vns()
[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']]
>>> vns.plotLearning()
```
The first output is the optimal solution found by the variable neighborhood search algorithm, and the second output is a graph of the weights calculated during each iteration against the iteration number.
### FunctionDef __init__(self, coords, stopping_iter)

Here is the documentation for the TSP class:

**TSP**: This module contains various classes and functions used to perform Traveling Salesman Problem (TSP) optimization.

Classes:

1. **SimulatedAnnealing**: The SimulatedAnnealing class is a child of the VariableNeighborhoodSearch class that uses simulated annealing as its optimization algorithm instead of variable neighborhood search. It inherits all methods from the parent class and adds some additional ones for simulated annealing-specific functionality.
2. **VariableNeighborhoodSearch**: The VariableNeighborhoodSearch class is a child of the TSP class that uses the variable neighborhood search algorithm to solve the TSP optimization problem. It inherits all methods from the parent class and adds some additional ones for variable neighborhood search-specific functionality.
3. **TSP**: This is the main class of this module that contains various functions for performing TSP optimization. It also acts as a container for other classes to inherit from.

Functions:

1. **nearestNeighbourSolution(dist_matrix)**: The nearestNeighbourSolution function takes in a distance matrix and returns a list of nodes that form a nearest-neighbor solution to the TSP problem. It does this by iteratively adding nodes to the current solution, selecting the nearest neighbor of the previous node based on the given distance matrix.
2. **weight(sol)**: The weight function takes in a tour (represented as a list of node indices) and returns its total weight (or distance) based on the distance matrix used to solve the TSP problem. It calculates the total distance between each pair of adjacent cities in the tour by summing up the distances between each pair.
3. **init(self, dist_matrix, num_cities, annealing_schedule=None)**: The init function is called upon class initialization to initialize a TSP object with a given distance matrix and number of cities. It also sets up some instance variables for the class such as the current best solution, current temperature, and some helper lists used in simulated annealing optimization.
4. **anneal(self, iterations=1000)**: The anneal function is called repeatedly to perform simulated annealing optimization using the nearest neighbor solution generated by the nearestNeighbourSolution function. It iteratively updates the current best solution based on a random walk of the nearest neighbor solution with the temperature schedule provided in the init function.
5. **vns(self, iterations=1000)**: The vns function is called repeatedly to perform variable neighborhood search optimization using the nearest neighbor solution generated by the nearestNeighbourSolution function. It iteratively updates the current best solution based on a random walk of the nearest neighbor solution with the temperature schedule provided in the init function.
6. **solve(self, iterations=1000)**: The solve function is called to perform TSP optimization using the nearest neighbor solution generated by the nearestNeighbourSolution function. It either performs simulated annealing optimization or variable neighborhood search optimization based on the selected algorithm.
7. **set_algorithm(self, alg='sa')**: The set_algorithm function allows the user to select which TSP optimization algorithm they want to use from a list of options (currently 'sa' for simulated annealing and 'vns' for variable neighborhood search). It sets the self.alg instance variable accordingly.
8. **get_solution(self)**: The get_solution function returns the current best solution found by the TSP optimization algorithm, which is a list of node indices representing a tour.
9. **get_best_solution(self)**: The get_best_solution function returns the best solution found by the TSP optimization algorithm, which is a list of node indices representing a tour. This is different from the current best solution in that it refers to the best solution ever found during the optimization process.
10. **get_algorithm(self)**: The get_algorithm function returns the selected TSP optimization algorithm chosen by the user using the set_algorithm function.
11. **get_distance_matrix()**: The get_distance_matrix function returns the distance matrix used to solve the TSP optimization problem. This is a list of lists, where each inner list represents a node and its neighbors with their corresponding distances.
12. **print_solution(self)**: The print_solution function prints the current best solution found by the TSP optimization algorithm, which is a list of node indices representing a tour.
13. **print_best_solution(self)**: The print_best_solution function prints the best solution ever found during the TSP optimization process, which is a list of node indices representing a tour. This is different from the current best solution in that it refers to the best solution ever found during the optimization process.
14. **print_algorithm(self)**: The print_algorithm function prints the selected TSP optimization algorithm chosen by the user using the set_algorithm function.
15. **print_distance_matrix()**: The print_distance_matrix function prints the distance matrix used to solve the TSP optimization problem. This is a list of lists, where each inner list represents a node and its neighbors with their corresponding distances.
***
### FunctionDef weight(self, sol)

**weight**: The function `weight` is used to calculate the total distance between each pair of cities in a given tour.

**Parameters**:

* `sol`: A list of city indices representing the tour to be evaluated.

**Code Description**: This function calculates the total distance of the tour by summing up the distances between each pair of adjacent cities in the tour. The distance matrix is used to look up the distance between each pair of cities. The function then returns the total distance of the tour.

This function is called by the `vns` class in the `VariableNeighborhoodSearch` module, which uses it to evaluate different tours and determine the best one based on its cost (or distance). This process is repeated until an optimal solution is found or a predetermined stopping criterion is reached.

**Note**: The weight function is a key part of the Variable Neighborhood Search algorithm, as it helps to guide the search towards better solutions by providing a way to evaluate and compare different tours based on their cost (or distance).

**Output Example**: A possible return value of this function might be `250`, representing the total distance of a tour that visits cities 0, 1, 2, 3, 4 in that order.
***
### FunctionDef shake(self, solution, k)

**shake**: The function of shake is to perform a randomized swapping operation on a given solution candidate.

**parameters**:

* `self`: A reference to the VariableNeighborhoodSearch class instance calling this method.
* `solution`: A list representing the current solution candidate being operated upon.
* `k`: An integer indicating the number of randomized swaps to perform on the given solution candidate.

**Code Description**: The shake function takes a VariableNeighborhoodSearch class instance and a list representing a current solution candidate as input, performs k randomized swaps on the given solution candidate, and returns the modified solution candidate. The function utilizes the randint method from the random module to generate two random indices within the range of the length of the solution candidate, which are then used to swap corresponding elements in the list.

The shake function is called by the VariableNeighborhoodSearch class instance during the neighbor search process as part of its neighborhood exploration strategy. By repeatedly applying this function on a given solution candidate, the algorithm can explore different solutions and potentially find better ones.

**Note**: The value of k in the shake function should be chosen carefully based on the specific problem being solved. A larger value of k may lead to more thorough exploration of the search space but also increase the computational complexity of the algorithm.

**Output Example**: If the input solution candidate is [1, 2, 3] and k = 2, the output could be [1, 3, 2].
***
### FunctionDef local_search(self, solution)

**local_search**: The function of local_search is to perform a local search on a given solution by swapping two adjacent cities to improve its cost (or distance).

**parameters**:

* `self`: A reference to the VariableNeighborhoodSearch object that called this method.
* `solution`: The current solution to be evaluated and improved upon.

**Code Description**: This function performs a local search on the given solution by swapping two adjacent cities. It starts by initializing a variable `best_solution` to the original solution, and then iterates over all possible pairs of adjacent cities (using a nested loop) and checks if swapping them can improve the cost (or distance). If it does, the function updates the `best_solution` accordingly. This process continues until no further improvement is possible, at which point the function returns the best solution found.

**Note**: The weight function used in this algorithm helps guide the search towards better solutions by providing a way to evaluate and compare different tours based on their cost (or distance).

**Output Example**: A possible return value of this function might be `['a', 'b', 'c', 'd', 'e']`, representing an improved solution that visits cities in the order ['a', 'b', 'c', 'd', 'e'].
***
### FunctionDef vns(self)

**Variable Neighborhood Search (VNS) Algorithm**
=============================================

The Variable Neighborhood Search (VNS) algorithm is an optimization technique used to find the shortest path between two cities in a given set of cities. This algorithm uses a neighborhood search strategy to explore different solutions and improve the current solution. The VNS algorithm is widely used in various fields such as logistics, transportation, and supply chain management.

**Parameters**
-------------
The VNS algorithm takes several parameters as input:

* `stopping_iter`: An integer indicating the maximum number of iterations to perform during the search process.
* `sample_size`: An integer indicating the number of randomized swaps to perform on a given solution candidate.
* `weight`: A function that calculates the total distance between each pair of cities in a given tour.

**Code Description**
-------------------------
The VNS algorithm starts by initializing two variables: `best_solution` and `worst_solution`. The `best_solution` variable is set to the initial solution, while the `worst_solution` variable is set to an empty list. The algorithm then iterates over a maximum number of iterations (`stopping_iter`) and performs the following steps for each iteration:

1. Generate a randomized swap on the current `best_solution`.
2. Calculate the new cost (distance) for the swapped solution using the `weight` function.
3. If the new cost is lower than the current best cost, update the `best_solution` variable with the new solution. Otherwise, update the `worst_solution` variable with the new solution.
4. Repeat steps 1 to 3 for a maximum number of randomized swaps (`sample_size`).
5. Update the current best cost and the current worst cost based on the updated `best_solution` and `worst_solution` variables.
6. Repeat steps 1 to 5 until the maximum number of iterations is reached or the current best cost does not improve further.

**Note**
------
The VNS algorithm uses a neighborhood search strategy to explore different solutions and improve the current solution. The algorithm starts with an initial solution and performs randomized swaps on the solution to explore different solutions. The algorithm updates the current best cost and the current worst cost based on the updated `best_solution` and `worst_solution` variables, respectively.

**Example**
---------
The following code snippet demonstrates how to use the VNS algorithm in Python:
```python
from math import sqrt

def vns(cities, stopping_iter=1000, sample_size=5):
    """Variable Neighborhood Search (VNS) Algorithm"""
    
    # Initialize variables
    best_solution = cities[:]
    worst_solution = []
    cost = sqrt(sum([(a - b) ** 2 for a, b in zip(best_solution, cities)]))
    
    # Iterate over maximum number of iterations
    for i in range(stopping_iter):
        
        # Generate randomized swap on the current best solution
        for _ in range(sample_size):
            a, b = randint(0, len(cities) - 1), randint(0, len(cities) - 1)
            new_solution = list(best_solution)
            new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
            
            # Calculate the new cost for the swapped solution
            new_cost = sqrt(sum([(a - b) ** 2 for a, b in zip(new_solution, cities)]))
            
            # Update the current best cost and worst cost based on the updated solution
            if new_cost < cost:
                best_solution = new_solution
                cost = new_cost
            else:
                worst_solution = new_solution
    
    return best_solution, cost, worst_solution
```
This code snippet demonstrates how to use the VNS algorithm to find the shortest path between two cities in a given set of cities. The `vns` function takes three parameters: `cities`, which is a list of cities; `stopping_iter`, which is an integer indicating the maximum number of iterations to perform during the search process; and `sample_size`, which is an integer indicating the number of randomized swaps to perform on a given solution candidate. The function returns the best solution found, the cost (distance) for the best solution, and the worst solution found.

**Conclusion**
--------------
The Variable Neighborhood Search (VNS) algorithm is a powerful optimization technique used to find the shortest path between two cities in a given set of cities. This algorithm uses a neighborhood search strategy to explore different solutions and improve the current solution. The VNS algorithm is widely used in various fields such as logistics, transportation, and supply chain management. In this documentation, we provided an overview of the VNS algorithm, its parameters, code description, and example usage.
***
### FunctionDef animateSolutions(self)

**animateSolutions**: The function of animateSolutions is to animate the solution over time using Matplotlib library. 
**parameters**:
* history: a list of solutions chosen by the algorithm
* points: an array_like of points with coordinates

This function creates a plot of the TSP using Matplotlib and animates it over time. The key frames are calculated based on the length of the history list divided by 100, and the animation is initialized with the first frame. Each frame updates the solution on the graph by plotting a line through all the nodes in the history list. This function is called by two other objects in the project: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions and TSP/vns.py/VariableNeighborhoodSearch/animateSolutions. Both of these functions are part of a larger algorithm for solving the Traveling Salesman Problem, and they use this function to visualize the solutions found by the algorithms.

**Note**: This code uses Matplotlib library to create a plot of the TSP solution over time, which requires the matplotlib library to be installed. Additionally, this code assumes that the points are 2D coordinates stored in an array_like format.
***
### FunctionDef plotLearning(self)

**plotLearning**: The function of plotLearning is to generate a visual representation of the learning process by plotting the weight list against the iteration number.

**parameters**: 
· self: Represents the VariableNeighborhoodSearch object instance.

**Code Description**: This Function uses Matplotlib library's plot() function to plot the weight list against the iteration number. The line_init and line_min variables are used to create a red and green horizontal lines, respectively, representing the initial weight and the optimized weight. The legend is created using the plt.legend() function, which displays the labels for the horizontal lines. The y-axis label and x-axis label are set using the plt.ylabel() and plt.xlabel(), respectively. Finally, the plot is shown using the plt.show() function.

This Function is called by the main() function in TSP/tsp_vns.py to visualize the learning process of the VariableNeighborhoodSearch algorithm. The calling relationship from a functional perspective is that the main() function calls the plotLearning() function, which plots the learning process visually.

**Note**: This Function assumes that the weight list and iteration number are stored in the self.weight_list and self.iteration variables, respectively. Therefore, it is important to ensure that these variables have been properly initialized before calling this Function.
***
