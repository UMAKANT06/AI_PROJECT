## FunctionDef vectorToDistMatrix(coords)

---

**vectorToDistMatrix**
=====================

The `vectorToDistMatrix` function creates a distance matrix from an input vector of coordinates. This function is used as part of the TSP problem, where the goal is to find the shortest path that visits all cities exactly once and returns to the starting city. The `vectorToDistMatrix` function takes a 2D numpy array of coordinates as its only parameter, and it returns a 2D numpy array representing the distance matrix between each pair of cities.

**Parameters**
--------------

The `vectorToDistMatrix` function takes a single parameter, which is a 2D numpy array of floats representing the coordinates of the cities. The number of rows in this array should be equal to the number of cities, and the number of columns in this array should be equal to the number of dimensions (2 for a city). For example, if we have a TSP problem with 5 cities, each represented by a 2D vector of floats, the input array would look like this:
```python
[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0], [9.0, 10.0]]
```
The function assumes that the input coordinates are valid and in the correct format. Invalid or malformed input may result in errors being raised during the execution of the function.

**Return Value**
--------------

The `vectorToDistMatrix` function returns a 2D numpy array representing the distance matrix between each pair of cities. The shape of this array is `(n, n)`, where `n` is the number of cities in the input vector. Each element of the array represents the Euclidean distance between the corresponding pair of cities, rounded to the nearest integer. For example, if we have a TSP problem with 5 cities and their coordinates are:
```python
[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0], [9.0, 10.0]]
```
The output distance matrix would look like this:
```python
[[0, 2.23606798, 3.1622776, 4.47213595, 5.0],
 [2.23606798, 0, 2.23606798, 3.84165736, 5.0],
 [3.1622776, 2.23606798, 0, 4.12310563, 5.0],
 [4.47213595, 3.84165736, 4.12310563, 0, 5.0],
 [5.0, 5.0, 5.0, 5.0, 0]]
```
The function assumes that the input coordinates are valid and in the correct format. Invalid or malformed input may result in errors being raised during the execution of the function.

**Edge Cases**
--------------

The `vectorToDistMatrix` function does not have any edge cases. However, it is important to note that the input coordinates must be valid and in the correct format for the function to produce accurate results. Invalid or malformed input may result in errors being raised during the execution of the function.

**Error Handling**
--------------

The `vectorToDistMatrix` function raises an error if the input coordinates are invalid or malformed. The error message will indicate what went wrong and how to fix it. For example, if the input array is not a 2D numpy array of floats, the function will raise a `TypeError` with the message "Input must be a 2D numpy array of floats."

**Notes**
--------

The `vectorToDistMatrix` function is used as part of the TSP problem, where the goal is to find the shortest path that visits all cities exactly once and returns to the starting city. The function assumes that the input coordinates are valid and in the correct format. Invalid or malformed input may result in errors being raised during the execution of the function.
## FunctionDef nearestNeighbourSolution(dist_matrix)

Documentation for nearestNeighbourSolution Function:
===============================================

Introduction:
-------------

The `nearestNeighbourSolution` function is a part of the TSP (Traveling Salesman Problem) solver and is used to compute an initial solution based on the nearest neighbour strategy. The function takes in a distance matrix as its input and returns a list of nodes that form the tour.

Parameters:
-------------

* `dist_matrix`: A two-dimensional array representing the distances between all pairs of nodes in the graph.

Returns:
---------

* A list of nodes that form the tour, where each node is visited exactly once and the tour starts and ends at the same node as the input matrix.

Code Description:
-------------------

The function starts by selecting a random starting node from the distance matrix using `random.randrange`. The `nodes_to_visit` list is then initialized with all the nodes in the graph except for the starting node. The nearest node to the starting node is found using the minimum distance between the starting node and each node in the `nodes_to_visit` list, and the function repeats this process until all nodes have been visited exactly once.

Notes:
-----

* If any of the input nodes in the distance matrix are not connected to each other (i.e., there is no path between them), the function will return an error.
* The function assumes that the distance matrix has a symmetric structure, meaning that the distances from node A to node B are the same as the distances from node B to node A. If this assumption is not met, the function may produce incorrect results.
* The function uses the `random.randrange` function to select a random starting node from the distance matrix, which means that the output tour will vary each time it is run. To obtain consistent results, the function can be modified to use a specific seed value for the random number generator.
* The function does not handle negative edge weights in the distance matrix, meaning that if any of the distances are negative, the function will return an error.
