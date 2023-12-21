class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        predecessors = {vertex: None for vertex in range(self.vertices)}
        distances[source] = 0

        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors


# New input graph
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(2, 1, -3)
g.add_edge(2, 4, 2)
g.add_edge(3, 5, 1)
g.add_edge(4, 3, 3)
g.add_edge(4, 5, 6)
g.add_edge(5, 1, -1)

source_vertex = 4
distances, predecessors = g.bellman_ford(source_vertex)

print("Shortest distances from source vertex", source_vertex)
print("\nVertex \tDistance \tPredecessor")
for vertex in range(g.vertices):
    print(f"{vertex}\t{distances[vertex]}\t\t{predecessors[vertex]}")
