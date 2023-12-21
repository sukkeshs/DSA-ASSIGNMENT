new_graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

visited_nodes = set()

def depth_first_search(visited, graph, current_node):
    if current_node not in visited:
        print(current_node)
        visited.add(current_node)
        for neighbor in graph[current_node]:
            depth_first_search(visited, graph, neighbor)

print("The Depth-First Search")
depth_first_search(visited_nodes, new_graph, 1)

