import random
import copy


class pathfinder:

    def __init__(self, matrix, point_ = None):
        self.point_visited = list()  # List to track the visited points in the path
        self.matrix = copy.copy(matrix)  # Copy the matrix to avoid modifying the original one
        self.forbidden_nextpoint = None  # Track the previous point to avoid revisiting it
        # Prepare the path-building process by setting the starting point
        if point_ is None:
            point_ = self.get_startpoint()
        self.point_visited = [point_]  # Initialize the visited points with the starting point
        self.point = point_


    def restore_Content(self):
        # Restore the content of the matrix in the event of a backtrack 
        self.matrix[self.point_visited[-1]][self.point_visited[-2]] = 1
        self.matrix[self.point_visited[-2]][self.point_visited[-1]] = 1

    # Find the available next points
    def get_nextpoint(self, point): 
        indices = list()
        for i, e in enumerate(self.matrix[point]):
            if e == 1 and i != self.forbidden_nextpoint:
                indices.append(i)
        print(point + 1, [i + 1 for i in indices])  # Print the current point and available next points
        if indices:
            return indices[-1]  # Choose a available next point (can be random.choice(indices))
        else:
            return None

    # Find a possible startpoint
    def get_startpoint(self):
        indices = list()
        for i, e in enumerate(self.matrix):
            if sum(e) % 2 == 1:     # Find the points with an odd number of connections to start the path
                indices.append(i)
        if indices:                 # Take any point if available
            return indices[0]
        else:
            return 0


    def built_path_step(self):
        if any(max(self.matrix)):
            # If there are still available connections in the matrix
            nextpoint = self.get_nextpoint(self.point)  # Get the next point to visit
            if nextpoint is not None:
                self.matrix[self.point][nextpoint] = 0  # Update the matrix to mark the connection as visited
                self.matrix[nextpoint][self.point] = 0
                self.point_visited.append(nextpoint)  # Add the next point to the visited points
                self.point = nextpoint  # Move to the next point
                self.forbidden_nextpoint = None
            else:
                self.point = self.point_visited[-2]  # Go back to the previous point
                self.restore_Content()  # Restore the matrix content
                self.forbidden_nextpoint = self.point_visited[-1]  # Avoid revisiting the previous point
                del self.point_visited[-1]  # Remove the last point from the visited points

        else:
            self.n = 0  # Terminate the path-building process

        return self.point_visited
