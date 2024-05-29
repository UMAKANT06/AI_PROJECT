## FunctionDef animateTSP(history, points)

Documentation for animateTSP Function:
--------------------------------------

The `animateTSP` function is used to animate the solution over time. It takes two parameters: `history` and `points`.

### Parameters

* `history`: list of lists, where each sublist represents a path chosen by the algorithm.
* `points`: array-like, containing the coordinates for each point in the graph.

### Returns

This function returns nothing. It is used to animate the pre-calculated solutions on the graph.

### Notes

* The animation will display approximately 100 frames for each solution chosen by the algorithm.
* The `key_frames_mult` variable is used to calculate the number of frames per solution, based on the length of the history list and a multiplier value of 100.
* The function initializes the node dots on the graph using the `init` function, which calculates the x- and y-coordinates for each point in the first sublist of the history list and sets the axes slightly larger to include all points.
* The `update` function is used to update the solution on the graph for each frame. It calculates the x- and y-coordinates for each point in the chosen path using the `history[frame]` value, which represents the current sublist of the history list being animated. It then sets the data for the line plot using these coordinates.
* The function uses `FuncAnimation` to animate the pre-calculated solutions, with an initial function of `init`, a frame range based on the length of the history list and the key frames multiplier value, and an interval time of 3 milliseconds between each update. The animation is set to repeat once.
* The function uses `plt.show` to display the graph with the animated solution.
### FunctionDef init

Documentation for init Function in TSP/animated_visualizer.py/animateTSP:
------------------------------------------------------------------------

init() is a function that initializes the node dots on the graph and draws axes slightly bigger than the original values. It also initializes an empty solution to be plotted later.

### Parameters:
N/A

### Return Value:
line, which is an empty tuple containing a line object that will be used to plot the solution.

### Notes:
* The function uses the `points` variable from the global scope to generate the x and y coordinates for the node dots.
* It uses the `history[0]` variable from the global scope to determine which points should be plotted as node dots on the graph.
* It sets the limits of the x-axis and y-axis slightly bigger than the original values using the `ax.set_xlim()` and `ax.set_ylim()` functions. This is done to ensure that the axes are not too small or too large, making it easier for users to visualize the graph.
* The function returns a tuple containing the line object used to plot the solution later in the program.

Testing Recommendations:
----------------------

1. Test different input values for the `points` variable to ensure that the x and y coordinates are correctly generated for node dots on the graph.
2. Test different input values for the `history[0]` variable to ensure that the correct points are plotted as node dots on the graph.
3. Test the limits of the x-axis and y-axis using a large dataset to ensure that they are not too small or too large, making it easier for users to visualize the graph.
4. Test the return value of the function to ensure that it contains the expected line object used to plot the solution later in the program.
5. Test different scenarios where the `init()` function is called multiple times in a row to ensure that it can handle this case correctly and only initialize the necessary variables once.
***
### FunctionDef update(frame)

Documentation for Update Function:
---------------------------------

The `update` function is responsible for updating the solution on the graph for every frame. This function takes a single parameter `frame`, which represents the current frame number.

### Parameter Description:

* `frame`: The current frame number, used to retrieve the appropriate solution from the `history` dictionary.

### Code Description:

The `update` function retrieves the points for the current frame from the `history` dictionary and generates a line plot of the solution on the graph. The line is created using the `set_data()` method of the `line` object, which updates its data to the new values provided. The `x` and `y` coordinates are calculated by taking the first element of the `points` array, followed by the elements at the indices in the `history[frame]` list, and then repeating the first element again.

### Return Value:

* `line`: The updated line object representing the solution on the graph for the current frame.

### Edge Cases:

* If the `frame` parameter is not an integer or a string representing an integer, the function will raise a `ValueError`.
* If the `history` dictionary does not contain the specified `frame`, the function will return a `KeyError`.

### Error Handling:

The function will raise a `ValueError` if the `frame` parameter is not an integer or a string representing an integer. The function will also raise a `KeyError` if the `history` dictionary does not contain the specified `frame`.

### Notes:

* The `update` function assumes that the `points` array and the `history` dictionary have been properly initialized beforehand.
* The function uses a list comprehension to create the `x` and `y` coordinates for the line plot, which is more efficient than using a loop for this task.
* The `set_data()` method of the `line` object is used to update its data to the new values provided, rather than creating a new line object each time the function is called. This reduces memory usage and improves performance.
***
