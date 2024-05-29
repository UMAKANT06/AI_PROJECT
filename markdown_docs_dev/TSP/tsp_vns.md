## FunctionDef main

obj: TSP/vns.py/VariableNeighborhoodSearch/animateSolutions
Document: 

**animateSolutions**: The function of animateSolutions is to animate the solution over time using Matplotlib library. 
**parameters**:
* history: a list of solutions chosen by the algorithm
* points: an array_like of points with coordinates

This function creates a plot of the TSP using Matplotlib and animates it over time. The key frames are calculated based on the length of the history list divided by 100, and the animation is initialized with the first frame. Each frame updates the solution on the graph by plotting a line through all the nodes in the history list. This function is called by two other objects in the project: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions and TSP/vns.py/VariableNeighborhoodSearch/animateSolutions. Both of these functions are part of a larger algorithm for solving the Traveling Salesman Problem, and they use this function to visualize the solutions found by the algorithms.

**Note**: This code uses Matplotlib library to create a plot of the TSP solution over time, which requires the matplotlib library to be installed. Additionally, this code assumes that the points are 2D coordinates stored in an array_like format.
==========
obj: TSP/vns.py/VariableNeighborhoodSearch/plotLearning
Document: 

**plotLearning**: The function of plotLearning is to generate a visual representation of the learning process by plotting the weight list against the iteration number.

**parameters**: 
· self: Represents the VariableNeighborhoodSearch object instance.

**Code Description**: This Function uses Matplotlib library's plot() function to plot the weight list against the iteration number. The line_init and line_min variables are used to create a red and green horizontal lines, respectively, representing the initial weight and the optimized weight. The legend is created using the plt.legend() function, which displays the labels for the horizontal lines. The y-axis label and x-axis label are set using the plt.ylabel() and plt.xlabel(), respectively. Finally, the plot is shown using the plt.show() function.

This Function is called by the main() function in TSP/tsp_vns.py to visualize the learning process of the VariableNeighborhoodSearch algorithm. The calling relationship from a functional perspective is that the main() function calls the plotLearning() function, which plots the learning process visually.

**Note**: This Function assumes that the weight list and iteration number are stored in the self.weight_list and self.iteration variables, respectively. Therefore, it is important to ensure that these variables have been properly initialized before calling this Function.
==========
