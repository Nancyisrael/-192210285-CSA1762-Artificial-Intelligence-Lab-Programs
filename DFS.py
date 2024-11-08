def dfs(graph, start, goal):
    stack, visited = [start], {start}
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return False

# Example graph as an adjacency list
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}

print("Path found!" if dfs(graph, 'A', 'F') else "No path found.")
