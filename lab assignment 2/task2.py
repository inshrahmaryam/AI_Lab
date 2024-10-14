import heapq

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def hill_climbing(maze, start, goal):
    current = start
    path = [current]
    cost = 0

    while current != goal:
        neighbors = get_neighbors(maze, current)
        best_neighbor = min(neighbors, key=lambda n: heuristic(n, goal), default=None)

        if best_neighbor is None or heuristic(best_neighbor, goal) >= heuristic(current, goal):
            break

        current = best_neighbor
        path.append(current)
        cost += 1

    return path, cost

def get_neighbors(maze, current):
    neighbors = []
    x, y = current
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

maze = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (9, 9)

path, cost = hill_climbing(maze, start, goal)
print(f"Path: {path}")
print(f"Cost: {cost}")