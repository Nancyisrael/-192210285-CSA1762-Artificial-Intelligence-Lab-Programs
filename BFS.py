def bfs(graph, start, goal):
    queue = [(start, [start])]  
    visited = {start}
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
path = bfs(graph, 'A', 'F')
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
