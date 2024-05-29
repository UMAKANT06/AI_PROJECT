## ClassDef VariableNeighborhoodSearch
Variable Neighborhood Search (VNS) is a class used for solving Traveling Salesman Problems (TSP). The __init__ method takes in a list of coordinates and an integer stopping iteration as arguments. It initializes the dist_matrix, curr_solution, best_solution, solution_history, iterative number, min_weight, weight_list, and initial_weight attributes. 
The local search function receives a candidate solution and returns a local search solution by swapping two adjacent nodes in the given solution. The shake method receives a current solution and an integer k as arguments and returns a random shaken solution of the candidate. The vns function uses a while loop to run until the stopping iteration is reached, where it iteratively shakes the current solution, updates its weight, and updates its best solution if the new weight is lower than the previous one. 
The animateSolutions method is used for visualizing the solutions; and the plotLearning method is used for plotting the learning process of the class instance. The variables are used to track the iterations, weight, solution history, and best solution during the vns execution.
### FunctionDef __init__(self, coords, stopping_iter)

Documentation for __init__ Function in TSP/vns.py/VariableNeighborhoodSearch Module:

Introduction:
The __init__ function is the constructor of the VariableNeighborhoodSearch class, which is used to initialize the variables and set up the necessary data structures for the optimization algorithm. The function takes two parameters: coords, which is a list of coordinates for the nodes in the TSP problem, and stopping_iter, which is the maximum number of iterations that the algorithm will perform before terminating.

Parameters:

* coords (list): List of coordinates for the nodes in the TSP problem.
* stopping_iter (int): Maximum number of iterations that the algorithm will perform before terminating.

Attributes:

* coords (list): Same as input parameter coords.
* sample_size (int): Number of nodes in the TSP problem.
* stopping_iter (int): Same as input parameter stopping_iter.
* iteration (int): Current iteration number, starting at 1.
* dist_matrix (numpy array): Distance matrix between all pairs of nodes in the TSP problem.
* curr_solution (list): Current solution vector for the TSP problem.
* best_solution (list): Best solution vector found so far for the TSP problem.
* solution_history (list): List containing all solutions vectors found during optimization.
* curr_weight (float): Weight of the current solution vector, calculated using the distance matrix and the weight function.
* initial_weight (float): Initial weight of the best solution vector, used for comparison during optimization.
* min_weight (float): Minimum weight found so far during optimization, used to determine termination conditions.
* weight_list (list): List containing all weights calculated during optimization.

Code Description:
The __init__ function first sets up the necessary data structures for the optimization algorithm by initializing the distance matrix and current solution vector using the input parameter coords. It then sets the best solution vector to be the same as the current solution vector, and initializes the list of weights calculated during optimization. The function also prints a message indicating that the variable neighborhood search algorithm is being used, and displays the initial weight of the current solution vector.

Notes:

* __init__ function should only be called once when creating an instance of the VariableNeighborhoodSearch class.
* Input parameters coords and stopping_iter must be valid lists or numpy arrays with appropriate dimensions for the TSP problem being optimized.
* The best_solution vector should be initialized to a feasible solution vector that is close to the optimal solution.
* The initial weight of the best_solution vector is used during optimization to determine termination conditions based on the minimum weight found so far.
***
### FunctionDef weight(self, sol)
Function Name: weight

Description: This function calculates the total weight of a given solution (sol) based on the distance matrix (dist_matrix) defined in the constructor of the VariableNeighborhoodSearch class. The weight is calculated by summing up the distances between all pairs of adjacent cities in the solution.

Parameters or Attributes:

* sol: A list of integers representing the cities visited in a particular order.
* dist_matrix: A two-dimensional list of floats where each element represents the distance between two adjacent cities. The first dimension corresponds to the source city and the second dimension corresponds to the destination city.

Code Description:
The weight function uses the zip() function in Python to iterate over all pairs of adjacent cities in the solution sol, and then calculates the sum of their corresponding distances using the dist_matrix.

Note: The weight function assumes that the input solution (sol) is a valid path in the graph represented by the distance matrix. If the input solution contains any repeated cities or invalid edges, the weight function may produce incorrect results. Therefore, it is important to test the function with a variety of inputs to ensure its correctness.
***
### FunctionDef shake(self, solution, k)

`shake()` is a function used to modify the solution of the `VariableNeighborhoodSearch` algorithm in the TSP/vns.py project by randomly swapping two nodes in the solution. This function takes two parameters:

* `solution`: A list of integers representing the current solution.
* `k`: An integer indicating the number of random swaps to perform on the solution.

The function first creates a copy of the input solution, and then performs `k` random swaps between nodes in the solution using the `random.randint()` method. Each swap involves exchanging the values of two nodes in the solution at random positions. After all swaps are performed, the modified solution is returned.

Note that the function assumes that the input `solution` is a valid solution for the TSP problem and that `k` is a positive integer. If either of these conditions is not met, an error may occur. Therefore, it is important to test the function with appropriate inputs to ensure correct behavior.

In terms of testing, the following edge cases should be considered:

* Testing with valid input solutions and varying values of `k` to check that the function correctly swaps nodes in the solution.
* Testing with invalid input solutions (e.g., a solution with negative weights or cycles) to ensure that the function handles such inputs appropriately.
* Testing with large values of `k` to check that the function can handle larger numbers of random swaps without causing performance issues.

In terms of error handling, it is important to ensure that the function gracefully handles invalid input parameters or unexpected errors during execution. This may involve using try-catch blocks or other error handling mechanisms to catch and report any exceptions that occur during the execution of the function.

Finally, in terms of return values, it is important to document the expected output of the function for different inputs. For example, if the input solution has `n` nodes, the function should return a modified solution with `n` nodes after performing the random swaps. It may also be helpful to provide examples of how the function can be used in practice, such as how it might be integrated with other parts of the TSP/vns.py project.

Overall, testing and documentation for the `shake()` function will help ensure that the function works correctly and provides reliable results when used within the context of the TSP/vns.py project.
***
### FunctionDef local_search(self, solution)

local_search() is a function in TSP/vns.py/VariableNeighborhoodSearch that searches for the best solution within a given sample size. The following are its parameters and attributes:

* Parameters:
	+ solution: list, the initial solution
	+ sample_size: int, the number of neighboring solutions to be considered
* Attributes:
	+ best_solution: list, the best solution found so far
	+ best_weight: float, the weight of the best solution found so far
	+ improved: bool, whether a better solution has been found or not.

The function works by iteratively swapping neighboring cities within the initial solution and evaluating their weights. If a better solution is found, it replaces the current best solution. The loop continues until no improvement is made in the weight of the solution. The final best solution is returned.

The key aspects for testing are as follows:

* Edge cases:
	+ Test the function with an empty list or tuple as input.
	+ Test the function with a list containing only one city.
	+ Test the function with a sample size of 1.
* Error handling:
	+ Test the function with a negative or zero value for sample_size.
	+ Test the function with an invalid weight function that returns a non-numeric value.
* Return values:
	+ Test the function with a valid input and check if it returns a list of cities representing the best solution found.
	+ Test the function with a valid input and check if it returns a float representing the weight of the best solution found.
	+ Test the function with an invalid input, such as a string or a list of cities that does not match the initial solution's structure, and check if it raises an error.

Overall, testing the local_search() function involves verifying its behavior in various scenarios, including edge cases, error handling, and return values. By thoroughly testing these aspects, testers can ensure that the function works as intended and provides accurate results for different inputs.
***
### FunctionDef vns(self)

Documentation for VNS Function:
==============================

The `vns` function is a key component of the Variable Neighborhood Search algorithm in our project. It is responsible for performing the actual search and optimization process, using the provided stopping criteria to determine when to terminate the search. The function takes no parameters but uses several attributes to store the current state of the search, including the current solution, weight, iteration count, and minimum weight found so far.

The `vns` function works as follows: it starts by initializing a counter variable `k` to 1 and entering a while loop that continues until the iteration count exceeds the provided stopping criteria. Within this while loop, it iteratively performs the following actions:

1. Generate a new candidate solution using the `shake` method with the current solution and the current iteration number.
2. Perform local search on the candidate solution using the `local_search` method.
3. Evaluate the weight of the candidate solution using the `weight` method.
4. If the weight is lower than the current minimum weight, update the current solution, minimum weight, and best solution accordingly.
5. Increment the iteration count by 1.
6. Append the weight to a list of weights and append the current solution to a list of solutions.

Once the while loop terminates, the function prints the minimum weight found and the improvement ratio between the initial weight and the minimum weight. The `vns` function returns nothing but instead modifies its attributes, making it suitable for testing.
***
### FunctionDef animateSolutions(self)

Documentation for animateSolutions Function:

The animateSolutions function is a part of the Variable Neighborhood Search (VNS) algorithm in TSP/vns.py. The purpose of this function is to visualize the evolution of solutions during the search process.

Function Description:

The animateSolutions function takes no input parameters and returns nothing. However, it utilizes a solution history that is passed as an argument when the VNS algorithm is initialized. It also requires coordinates (coords) for the nodes in the problem. The function animates these solutions using the animated_visualizer module.

Parameters or Attributes:

* solution_history: a list of lists containing the best solutions found by the algorithm during its search process. Each sublist represents a single solution and contains the node indices in the order they appear on the tour.
* coords: a dictionary mapping each node index to its corresponding coordinates (x, y) in the plane.

Code Description:

The animateSolutions function begins by using the animated_visualizer module to generate an animation of the given solution history and coordinates. It then loops through each sublist in the solution history and adds a new frame to the animation for each solution. Each frame includes the coordinates of the nodes and their connections, as well as the current cost of the tour.

Notes:

* Edge Cases: None.
* Error Handling: The function does not handle any errors that may occur during the creation of the animation. If any issues arise during this process, they will be reflected in the final output of the animated visualization.
* Return Values: None.

Conclusion:
The animateSolutions function is an essential part of the Variable Neighborhood Search (VNS) algorithm's visualization feature. It utilizes the animated_visualizer module to create a dynamic animation that shows the evolution of solutions during the search process. The function takes no input parameters and returns nothing, but it requires a solution history and coordinates for the nodes in the problem. The code description provides a detailed overview of the function's functionality, including its parameters, attributes, and return values.
***
### FunctionDef plotLearning(self)

plotLearning(self): Plots the learning progress of the algorithm
-----------------------------------------------

### Function Description:

This function plots the learning progress of the algorithm using matplotlib library's plotting functions. The weight list is plotted against the iteration number, with two horizontal lines representing the initial and optimized weights, respectively. The legend shows these two lines with corresponding labels.

The function takes no input arguments but relies on self attributes for its execution.

### Edge Cases:

* There are no edge cases to consider when testing this function.

### Error Handling:

* If the matplotlib library is not installed, an error will occur while executing this function.
* The function assumes that the weight_list and initial_weight attributes exist in self. If they do not exist or have not been defined, the function will raise an exception.
* If the min_weight attribute does not exist in self, the function will use the default value of 0 for plotting the optimized weight.

### Return Values:

* The function returns nothing but instead modifies the state of the self object by adding a new figure to the matplotlib library's pyplot.

### Testing Considerations:

* When testing this function, it is essential to ensure that the plot is displayed correctly on screen and that the horizontal lines represent the initial and optimized weights with their corresponding labels.
* To test for edge cases, one can input a weight_list with only two values (initial and optimized) to ensure that the function can still generate a valid plot even when there are only two weights to compare.
* The function assumes that the self object has been properly initialized with the required attributes. Therefore, testing this function requires initializing self with proper attributes before calling this function.
***
