board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

dictionary = {'START', 'NOTE', 'SAND', 'STONED'}

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def is_valid(x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def dfs(board, node, x, y, path, visited, found_words):
    path += board[x][y]
    visited.add((x, y))

    if path in dictionary:
        found_words.add(path)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (nx, ny) not in visited:
            dfs(board, node, nx, ny, path, visited, found_words)

    visited.remove((x, y))

def find_words(board, dictionary):
    found_words = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, None, i, j, "", set(), found_words)
    return found_words

valid_words = find_words(board, dictionary)
print("Valid words found:", valid_words)
