# Eulerpath
A small Python program that finds an  Eulerpath through a given matrix.

## Usage
To use this program run to GUI.py. Feel free to change the _adjacency_matrix_

## Algorithm
The pathfinding algorithm used in the Pathfinder program follows these steps:

1. Initialize the pathfinder class with the given _adjacency_matrix_.

2. Determine the starting point for the path by finding point with an odd number of connections.

3. Begin the path-building process by setting the starting point and marking it as visited.

4. While there are still available connections in the matrix:

    - Find the next available point to visit from the current point. Choose the last available point in the list of connections to create a more randomized path.
    - Update the matrix to mark the connection as visited.
    - Add the next point to the list of visited points.
    - Move to the next point and repeat the process.
5. If there are no more available connections, terminate the path-building process.

6. Return the list of visited points, representing the path through the matrix.

The algorithm ensures that all connections are visited exactly once while avoiding revisiting any connection. It also takes into account the starting point with an odd number of connections to ensure the path starts and ends at the same point.