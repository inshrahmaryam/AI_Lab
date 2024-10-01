graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 111, 'Sibiu': 140},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Zerind': 71},
    'Timisoara': {'Arad': 111, 'Lugoj': 70},
    'Lugoj': {'Timisoara': 70, 'Mehadia': 75},
    'Mehadia': {'Lugoj': 75, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 75},
    'Craiova': {'Drobeta': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 146},
    'Pitesti': {'Rimnicu Vilcea': 146, 'Bucharest': 101},
    'Bucharest': {'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Vaslui': {'Iasi': 92},
    'Fagaras': {'Sibiu': 99}
}
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    # Add the current node to the path
    path.append(start)
    visited.add(start)
    
    # Check if we have reached the goal
    if start == goal:
        return path
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path[:], visited)
            if result is not None:
                return result

    return None

# Find the path from Arad to Bucharest
start_city = 'Arad'
goal_city = 'Bucharest'
path = dfs(graph, start_city, goal_city)

if path:
    print("Path from Arad to Bucharest:", " -> ".join(path))
else:
    print("No path found from Arad to Bucharest.")
