import pygame
from collections import deque

# Initialize Pygame
pygame.init()

# Define constants
TILE_SIZE = 50  # Size of each tile
ROWS, COLS = 8, 8  # Maze dimensions
SCREEN_WIDTH = COLS * TILE_SIZE
SCREEN_HEIGHT = ROWS * TILE_SIZE

# Colors
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")

# Maze structure (1 = path, 0 = obstacle)
maze = [
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Start and goal positions
start = [3, 3]  # Set to the middle of the maze (list for mutability)
goal = (0, 5)

# Directions for moving in the maze (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS Algorithm to find the shortest path
def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([tuple(start)])  # Use tuple for immutability
    visited = set([tuple(start)])
    parent = {tuple(start): None}
    
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path
        
        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            new_pos = (new_row, new_col)
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 1 and new_pos not in visited):
                queue.append(new_pos)
                visited.add(new_pos)
                parent[new_pos] = current
    
    return None  # No path found

# Visualize the game
def draw_maze(maze, path):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE
            if maze[row][col] == 0:
                color = GRAY
            pygame.draw.rect(screen, color, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, BLACK, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    
    # # Draw path
    # if path:
    #     for pos in path:
    #         pygame.draw.circle(screen, BLUE, (pos[1] * TILE_SIZE + TILE_SIZE // 2, pos[0] * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 4)
    
    # Draw start and goal
    pygame.draw.circle(screen, YELLOW, (start[1] * TILE_SIZE + TILE_SIZE // 2, start[0] * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)
    pygame.draw.circle(screen, RED, (goal[1] * TILE_SIZE + TILE_SIZE // 2, goal[0] * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)

def main():
    clock = pygame.time.Clock()
    path = bfs(maze, tuple(start), goal)  # Find the path using BFS
    running = True

    while running:
        screen.fill(WHITE)
        draw_maze(maze, path)  # Draw the maze with the BFS path
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_pos = (start[0] - 1, start[1])
                    if maze[new_pos[0]][new_pos[1]] == 1:  # Check if move is valid
                        start[0] -= 1
                elif event.key == pygame.K_DOWN:
                    new_pos = (start[0] + 1, start[1])
                    if maze[new_pos[0]][new_pos[1]] == 1:
                        start[0] += 1
                elif event.key == pygame.K_LEFT:
                    new_pos = (start[0], start[1] - 1)
                    if maze[new_pos[0]][new_pos[1]] == 1:
                        start[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    new_pos = (start[0], start[1] + 1)
                    if maze[new_pos[0]][new_pos[1]] == 1:
                        start[1] += 1
        
        pygame.display.flip()
        clock.tick(30)  # Set frame rate

    pygame.quit()

if __name__ == "__main__":  # Corrected this line
    main()
