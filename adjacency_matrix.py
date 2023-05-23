import numpy as np
import random

def create_adj_matrix(num_vertices = 10, path_leght = 32):
    # Create an empty adjacency matrix
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    # Define the Eulerian path (vertices)
    euler_path = []
    for i in range(path_leght):
        euler_path.append(random.randint(1, num_vertices))

    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    # Add edges to the adjacency matrix based on the Eulerian path
    for i in range(len(euler_path) - 1):
        source = euler_path[i] - 1
        target = euler_path[i + 1] - 1

        # Avoid self-connections
        if source != target:
            adj_matrix[source][target] = 1

    return adj_matrix.tolist(), euler_path

#print("Adjacency Matrix:")
#adj_matrix_o, euler_path_o = create_adj_matrix()
#print(adj_matrix_o)
#print(euler_path_o)
