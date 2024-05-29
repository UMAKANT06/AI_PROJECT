## FunctionDef animateTSP(history, points)

**animateTSP**: The function of animateTSP is to animate the solution over time.

**parameters**:

* history: a list of solutions chosen by the algorithm
* points: an array_like of points with coordinates

**Code Description**: This code creates a plot of the TSP using Matplotlib and animates it over time. The key frames are calculated based on the length of the history list divided by 100, and the animation is initialized with the first frame. Each frame updates the solution on the graph by plotting a line through all the nodes in the history list.

This function is called by two other objects in the project: TSP/simulated_annealing.py/SimulatedAnnealing/animateSolutions and TSP/vns.py/VariableNeighborhoodSearch/animateSolutions. Both of these functions are part of a larger algorithm for solving the Traveling Salesman Problem, and they use this function to visualize the solutions found by the algorithms.

**Note**: This code uses Matplotlib to create a plot of the TSP solution over time, which requires the matplotlib library to be installed. Additionally, this code assumes that the points are 2D coordinates stored in an array_like format.

**Output Example**: A possible appearance of the code's return value could be a visual representation of the Traveling Salesman Problem solution animated over time.
### FunctionDef init

**init**: This is an initialization function for creating visualizations of TSP solutions using Matplotlib. 

**Parameters**:
* `history`: A list containing the history of the TSP problem being solved.
* `points`: A dictionary with the coordinates of the points in the graph, where each point has a unique key.
* `line`: The line object for plotting the solution path.

**Code Description**:
The function initializes node dots on the graph using the `x` and `y` lists, which are generated from the coordinates of the points in the `points` dictionary. It then plots the points as a circle (`'co'`), sets the axes limits to be slightly bigger than the range of the x- and y-coordinates, initializes the solution line to an empty list, and returns it.

**Note**: The function assumes that the `history` parameter contains at least one element, which corresponds to the initial state of the TSP problem.

**Output Example**:
```python
history = [
    [0, 1, 2, 3, 4], # initial state
    [1, 2, 3, 4, 5], # first step
    [2, 3, 4, 5, 6] # second step
]
points = {
    0: (0, 0),
    1: (1, 1),
    2: (2, 2),
    3: (3, 3),
    4: (4, 4),
    5: (5, 5),
    6: (6, 6)
}
line = None # initial value

# plot the TSP solution path using init() function
line = init(history, points)
```
In this example, the `init()` function is called with the `history` list and `points` dictionary as input. The output is a line object that can be used to visualize the solution path of the TSP problem.
***
### FunctionDef update(frame)

**update**: The function of update is to update the solution on the graph for every frame.

**parameters**: 

* frame: The frame number.

**Code Description**: This function updates the solution on the graph for each frame by using the history of points in a TSP problem. It first generates a list of x-coordinates and y-coordinates for the line representing the solution, then sets the data for the line using the matplotlib library's set_data() method. Finally, it returns the updated line object.

**Note**: This function assumes that the history variable contains the previous points in the TSP problem. It also assumes that the line object has already been created and initialized.

**Output Example**: A possible appearance of the code's return value could be a matplotlib line object with updated data for the solution on the graph.
***
