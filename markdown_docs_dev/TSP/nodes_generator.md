## ClassDef NodeGenerator

**NodeGenerator Class Documentation**

The NodeGenerator class is a Python class that generates random nodes (i.e., x-y coordinates) within a given rectangle, specified by width and height parameters. The generated nodes are stored in a numpy array with two columns, representing the x-coordinates and y-coordinates of each node, respectively.

**Function**: The NodeGenerator class has one primary function, which is to generate random nodes within a given rectangle. This function is used by other classes in the project that require generating nodes for their respective purposes.

**Attributes**:

* width: The width of the rectangle where the nodes will be generated. It is an integer value.
* height: The height of the rectangle where the nodes will be generated. It is an integer value.
* nodesNumber: The number of nodes that need to be generated. It is also an integer value.

**Code Description**: The NodeGenerator class uses NumPy's random.randint() function to generate random x-coordinates and y-coordinates within the specified rectangle. The generated nodes are then returned as a numpy array with two columns, representing the x-coordinates and y-coordinates of each node, respectively.

**Note**: This class is designed to be used in conjunction with other classes that require generating nodes for their respective purposes. It is not intended for standalone use.

**Output Example**: A possible appearance of the code's return value could be a numpy array with two columns, representing x-coordinates and y-coordinates of generated nodes, such as [[34, 85], [12, 67], ...].

**Caller Relationship**: This class is called by other classes in the project that require generating nodes for their respective purposes. For example, TSP/tsp_sa.py and TSP/tsp_vns.py both use NodeGenerator to generate nodes for their respective TSP algorithms.

In conclusion, the NodeGenerator class provides a simple way to generate random nodes within a given rectangle for use in other classes in the project that require generating nodes for their respective purposes. It is not intended for standalone use and should be used in conjunction with other classes that require generating nodes for their respective purposes.
### FunctionDef __init__(self, width, height, nodesNumber)

**__init__: Initialize NodeGenerator Object**

The `__init__` function is used to initialize a `NodeGenerator` object. It takes three parameters: `width`, `height`, and `nodesNumber`.

* `width`: The width of the generated nodes.
* `height`: The height of the generated nodes.
* `nodesNumber`: The number of nodes to be generated.

The function sets these values as attributes of the `NodeGenerator` object, which can then be used later in the program.

**Code Description:** The `__init__` function is a constructor method that is called when an instance of the `NodeGenerator` class is created. It initializes the object with the necessary parameters and sets them as attributes so they can be used later in the program.

**Note:** It's important to note that the `NodeGenerator` class is responsible for generating a list of nodes based on the given width, height, and number of nodes. The `__init__` function initializes the object with these parameters, which are then used by other methods in the class to generate the desired list of nodes.
***
### FunctionDef generate(self)

**generate**: The function of generate is to randomly generate node coordinates within the given bounds of the graph.

**parameters**:

* self (NodeGenerator): An instance of the NodeGenerator class, used to generate nodes with specific properties.
* width (int): The maximum value that x-coordinates can take.
* height (int): The maximum value that y-coordinates can take.
* nodesNumber (int): The number of nodes to be generated.

**Code Description**: The code uses NumPy's random module to generate node coordinates within the given bounds. Specifically, it generates a list of x-coordinates and a list of y-coordinates separately, each with a length equal to nodesNumber. Then, it stacks these two lists into a single array using np.column_stack(). The resulting array contains the coordinates of the generated nodes.

The function is called by the main functions in TSP/tsp_sa.py and TSP/tsp_vns.py, which are respectively used for simulated annealing and vehicle routing problems to solve the traveling salesman problem. The output of this function serves as the initial population of nodes for these algorithms.

**Note**: This function assumes that the width and height of the graph are both positive integers, and that the nodesNumber parameter is also a positive integer. If any of these conditions are not met, the generated coordinates may be invalid or cause errors in the calling code. Therefore, it is important to ensure that the parameters are properly validated before calling this function.

**Output Example**: A possible appearance of the code's return value could be a 2D array containing several rows and columns of random node coordinates within the given bounds. For example, a 3x2 array with values like:
```python
array([[50, 89], [16, 47], [75, 12]])
```
This output represents three nodes with x-coordinates between 0 and 100 and y-coordinates between 0 and 100.
***
