# dfs.py - Thuật toán tìm kiếm theo chiều sâu (DFS)
# Ghost: Pink

from utils import is_valid, reconstruct_path

# Các hướng di chuyển: trái, phải, lên, xuống
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(grid, start, goal):
    stack = [start]           # dùng stack thay vì queue
    visited = set()
    parent = {}
    expanded_nodes = 0

    visited.add(start)

    while stack:
        current = stack.pop()
        expanded_nodes += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, visited, expanded_nodes

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            next_pos = (nx, ny)

            if is_valid(nx, ny, grid) and next_pos not in visited:
                visited.add(next_pos)
                parent[next_pos] = current
                stack.append(next_pos)

    return None, visited, expanded_nodes  # không tìm được
