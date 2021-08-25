# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate,
# return the minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down, and right.
# You cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
#  [t, t, f, t],
#  [f, f, f, f],
#  [f, f, f, f]]
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach
# the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.


def grid_to_adjacency_dict_uniform_weight(grid):
    M = len(grid)
    N = len(grid[0])

    adj_dict = dict()
    for i in range(0, M * N):
        adj_dict[i] = dict()

    for i in range(0, M):
        for j in range(0, N):
            if grid[i][j]:
                continue

            n = i * N + j
            if i > 0 and not grid[i - 1][j]:
                adj_dict[n][n - N] = True
            if j > 0 and not grid[i][j - 1]:
                adj_dict[n][n - 1] = True
            if j < (N - 1) and not grid[i][j + 1]:
                adj_dict[n][n + 1] = True
            if i < (M - 1) and not grid[i + 1][j]:
                adj_dict[n][n + N] = True

    return adj_dict


inf = 10 ** 6


def dijkstra(adj_dict, start, end):
    unvisited, visited = {i: inf for i in range(0, len(adj_dict))}, dict()
    unvisited[start] = 0  # a distance of 0 to itself

    while unvisited:
        u = min(unvisited, key=unvisited.get)
        for neighbour in adj_dict[u]:
            if neighbour in unvisited:
                d = unvisited[u] + 1
                if d < unvisited[neighbour]:
                    unvisited[neighbour] = d
        visited[u] = unvisited.pop(u)

    return visited[end] + 1


t = True
f = False

# [[f, f, f, f],
#  [t, t, f, t],
#  [f, f, f, f],
#  [f, f, f, f]]
grid = [[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]]
assert 7 == dijkstra(
    grid_to_adjacency_dict_uniform_weight(grid), 0, len(grid) * len(grid[0]) - 1
)

# [[f, f, t, f, f, f],
#  [f, f, t, f, t, f],
#  [f, f, t, f, t, f],
#  [f, f, f, f, t, f]]
grid = [[f, f, t, f, f, f], [f, f, t, f, t, f], [f, f, t, f, t, f], [f, f, f, f, t, f]]
assert 15 == dijkstra(
    grid_to_adjacency_dict_uniform_weight(grid), 0, len(grid) * len(grid[0]) - 1
)
