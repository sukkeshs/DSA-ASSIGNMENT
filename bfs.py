def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Test Case 1
graph1 = {
    'X': ['Y', 'Z', 'W'],
    'Y': ['X'],
    'Z': ['X', 'W'],
    'W': ['X', 'Z', 'V'],
    'V': ['W'],
}
print("BFS Traversal - Test Case 1:")
bfs(graph1, 'X')
print("\n")

# Test Case 2
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
print("BFS Traversal - Test Case 2:")
bfs(graph2, 'A')
