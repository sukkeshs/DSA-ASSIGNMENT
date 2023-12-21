import heapq

INF = 9999999
V = 5

# Sample input graph
G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Priority queue to store edges
edge_queue = []

# Start from vertex 0
for j in range(V):
    if G[0][j] > 0:
        heapq.heappush(edge_queue, (G[0][j], 0, j))

selected = set()
selected.add(0)

print("Edge : Weight\n")
while len(selected) < V:

    weight, x, y = heapq.heappop(edge_queue)

    if y not in selected:
        print(str(x) + "-" + str(y) + ":" + str(weight))
        selected.add(y)

        for j in range(V):
            if G[y][j] > 0 and j not in selected:
                heapq.heappush(edge_queue, (G[y][j], y, j))
