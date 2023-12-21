# Library for infinity
infinity = float('inf')


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(chr(97 + node), "\t\t ", dist[node], "\n")

    def minDistance(self, dist, sptSet):
        min_val = infinity
        min_index = -1

        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        dist = [infinity] * self.V
        dist[src] = 0
        count = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, count)
            count[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and count[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)


g = Graph(5)
g.graph = [
    [0, 8, 0, 3, 0],
    [8, 0, 2, 5, 0],
    [0, 2, 0, 0, 7],
    [3, 5, 0, 0, 1],
    [0, 0, 7, 1, 0]
]

g.dijkstra(0)

# Updated test case graph
g = Graph(5)
g.graph = [
    [0, 6, 0, 2, 0],
    [6, 0, 3, 0, 0],
    [0, 3, 0, 1, 4],
    [2, 0, 1, 0, 5],
    [0, 0, 4, 5, 0]
]

g.dijkstra(0)

