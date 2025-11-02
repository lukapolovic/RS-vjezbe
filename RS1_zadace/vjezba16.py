graph = {
'A': [('B', 1), ('C', 4)],
'B': [('A', 1), ('C', 2), ('D', 5)],
'C': [('A', 4), ('B', 2), ('D', 1)],
'D': [('B', 5), ('C', 1)]
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        unvisited_nodes = {node: distances[node] for node in graph if node not in visited}
        if not unvisited_nodes:
            break
        current_node = min(unvisited_nodes, key=unvisited_nodes.get)
        current_distance = distances[current_node]

        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        visited.add(current_node)

    return distances

print(dijkstra(graph, 'A'))