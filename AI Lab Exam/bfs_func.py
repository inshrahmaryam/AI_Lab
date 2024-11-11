from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B'],
    'B': ['C', 'H'],
    'C': ['D', 'G'],
    'D': ['E'],
    'E': ['F'],
    'H': ['I', 'J', 'M'],
    'J': ['K'],
    'K': ['L']
}

# Function to perform BFS and find the shortest path
def bfs_find_path(graph, start, goal):
    queue = deque([[start]])  # Queue to store paths
    visited = set()  # Set to keep track of visited nodes

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        node = path[-1]  # Get the last node in the path

        # If we reached the goal, return the path
        if node == goal:
            return path

        # Mark the node as visited and add neighbors to the queue
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]  # Create a new path
                queue.append(new_path)

    return None  # Return None if no path is found

# Find and print the path from A to L
path = bfs_find_path(graph, 'A', 'L')
print("Path from A to L:", " -> ".join(path) if path else "No path found")