grid = {
    'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
    'F': (1, 0), 'G': (1, 1), 'H': (2, 0), 'I': (2, 1), 'J': (2, 2), 'K': (2, 3), 'L': (2, 4),
    'M': (3, 0), 'N': (3, 1), 'O': (3, 2), 'P': (3, 3), 'Q': (3, 4),
    'R': (4, 0), 'S': (4, 1), 'T': (4, 2), 'U': (4, 3), 'V': (4, 4),
    'W': (5, 0), 'X': (5, 1), 'Y': (5, 2)
}

def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def get_neighbors(node):
    neighbors = []
    r, c = grid[node]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        # Check if new coordinates exist in the grid values
        for key, value in grid.items():
            if value == (new_r, new_c):
                neighbors.append(key)
    return neighbors

def hill_climbing(start, goal):
    current = start
    path = [current]
    
    while current != goal:
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        
        # Select the neighbor closest to the goal
        best_neighbor = min(neighbors, key=lambda n: manhattan_distance(grid[n], grid[goal]))
        
        # If no progress is made towards the goal, stop the search
        if manhattan_distance(grid[best_neighbor], grid[goal]) >= manhattan_distance(grid[current], grid[goal]):
            break
        
        current = best_neighbor
        path.append(current)
    
    return path

start_node = 'A'
goal_node = 'Y'
path = hill_climbing(start_node, goal_node)
print(f"Path from {start_node} to {goal_node}: {path}")
