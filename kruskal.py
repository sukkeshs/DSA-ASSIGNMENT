def kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

  
    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v

  
    mst = []

    #
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight)) 
    return mst

new_graph = {
    'A': {'B': 5, 'C': 8},
    'B': {'A': 5, 'C': 6, 'D': 4},
    'C': {'A': 8, 'B': 6, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

result = kruskal(new_graph)
print("(Kruskal's Algorithm- Edges in Minimum Spanning tree :")
for u, v, weight in result:
    print(f"{u} - {v}: {weight}")
