from collections import deque

# Define the graph as a dictionary
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

def bfs(graph, start, goal):
    # Create a queue for BFS
    queue = deque([(start, [start])])  # queue holds tuples of (current_node, path)

    while queue:
        current_node, path = queue.popleft()

        # Check if we have reached the goal
        if current_node == goal:
            return path

        # Iterate through neighbors
        for neighbor in graph[current_node]:
            if neighbor not in path:  # Check if not visited
                queue.append((neighbor, path + [neighbor]))

    return None  # Return None if no path is found

# Find the path from Arad to Bucharest using BFS
start_city = 'Arad'
goal_city = 'Bucharest'
path = bfs(graph, start_city, goal_city)

if path:
    print("Path from Arad to Bucharest:", " -> ".join(path))
else:
    print("No path found from Arad to Bucharest.")
