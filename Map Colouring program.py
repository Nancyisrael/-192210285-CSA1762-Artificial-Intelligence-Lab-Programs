def is_valid(node, color, graph, colors):
    return all(colors.get(nei) != color for nei in graph[node])
def map_coloring(graph, colors_avail, colors={}):
    if len(colors) == len(graph):
        return colors
    node = [n for n in graph if n not in colors][0]
    for color in colors_avail:
        if is_valid(node, color, graph, colors):
            colors[node] = color
            if map_coloring(graph, colors_avail, colors):
                return colors
            del colors[node]
    return None
graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
colors_avail = ['Red', 'Green', 'Blue']
print(map_coloring(graph, colors_avail))
