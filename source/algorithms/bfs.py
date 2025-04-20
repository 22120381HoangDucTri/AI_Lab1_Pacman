# bfs.py - thuật toán tìm đường BFS cho Blue Ghost

from collections import deque
from utils import is_valid, reconstruct_path

# Các hướng di chuyển: trái, phải, lên, xuống
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(grid, start, goal):
    visited = set()
    queue = deque()
    parent = {}
    expanded_nodes = 0

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        expanded_nodes += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, visited, expanded_nodes  # thêm visited

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = current
                queue.append((nx, ny))

    return None, visited, expanded_nodes

