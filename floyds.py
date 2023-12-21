import networkx as nx
import matplotlib.pyplot as plt

# Set a constant for infinity
INF = 999999

def floyd_warshall(graph):
    # Copy the graph to avoid modifying the original
    distance = [row[:] for row in graph]

    # The number of vertices
    v = len(graph)

    # Iterating over vertices individually
    for k in range(v):
        for i in range(v):
            for j in range(v):
                # Update distance if a shorter path is found
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Print the solution
    print_solution(distance)

    # Plot the graph
    plot_graph(graph, "Original Graph")
    plot_graph(distance, "Shortest Path Graph")

# Printing the solution
def print_solution(distance):
    print("Shortest distances between every pair of vertices:")
    for i in range(len(distance)):
        for j in range(len(distance[i])):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print("")

# Function to convert adjacency matrix to networkx graph
def convert_to_networkx(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != INF:
                G.add_edge(i, j, weight=graph[i][j])
    return G

# Plotting the graph
def plot_graph(graph, title):
    G = convert_to_networkx(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', width=1)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title(title)
    plt.show()

# Test case 1
G = [
    [0, 11, INF, 5],
    [4, 0, INF, 2],
    [INF, 7, 0, INF],
    [INF, INF, 9, 0]
]

print("Test case 1:")
floyd_warshall(G)
