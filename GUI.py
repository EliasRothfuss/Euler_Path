import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
import Euler_path
import adjacency_matrix

#auto mode
#adj_matrix, euler_path = adjacency_matrix.create_adj_matrix(5,10)
#print(euler_path)

# Define the adjacency matrix
adj_matrix = [
    [0,1,0,1,1],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [1,1,1,0,1],
    [1,1,0,1,0]
    ]
# Create a graph object
G = nx.Graph()

# Add nodes to the graph
num_nodes = len(adj_matrix)
G.add_nodes_from(range(1, num_nodes+1))

# Add edges to the graph based on the adjacency matrix
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix[i][j] == 1:
            G.add_edge(i+1, j+1)

# Plot the graph
fig = plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)
def create_graph():
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray')

path_obj = Euler_path.pathfinder(adj_matrix)
path = path_obj.built_path()
path = [e + 1 for e in path]
print (path)
def animate_path(frame):
    if frame < len(path)-1:
        path_edges = list(zip(path[:-1], path[1:frame+2]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0)
    else: 
        plt.clf()  # Clear the current plot
        create_graph()

create_graph()
ani = FuncAnimation(fig, animate_path, frames=len(path), interval=1000, repeat=True)
plt.show()
