## FunctionDef main

==========
obj: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions
Document: 

**animateSolutions**: The function of animateSolutions is to animate the solution over time.

**Parameters**:

* history: a list of solutions chosen by the algorithm
* points: an array_like of points with coordinates

**Code Description**: This code creates a plot of the TSP using Matplotlib and animates it over time. The key frames are calculated based on the length of the history list divided by 100, and the animation is initialized with the first frame. Each frame updates the solution on the graph by plotting a line through all the nodes in the history list.

This function is called by two other objects in the project: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions and TSP/vns.py/VariableNeighborhoodSearch/animateSolutions. Both of these functions are part of a larger algorithm for solving the Traveling Salesman Problem, and they use this function to visualize the solutions found by the algorithms.

**Note**: This code uses Matplotlib to create a plot of the TSP solution over time, which requires the matplotlib library to be installed. Additionally, this code assumes that the points are 2D coordinates stored in an array_like format.

**Output Example**: A possible appearance of the code's return value could be a visual representation of the Traveling Salesman Problem solution animated over time.
==========

