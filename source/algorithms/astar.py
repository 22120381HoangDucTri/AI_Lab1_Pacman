# astar.py - Thuật toán A* Search
# Ghost: Red

import heapq
from utils import is_valid, reconstruct_path

# Di chuyển 4 hướng (Manhattan)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan(a, b):
    """Hàm heuristic: khoảng cách Manhattan"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    heap = [(0 + manhattan(start, goal), 0, start)]  # (f, g, node)
    visited = set()
    parent = {}
    g_cost = {start: 0}
    expanded_nodes = 0

    while heap:
        f, cost, current = heapq.heappop(heap)
        expanded_nodes += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, visited, expanded_nodes

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            next_pos = (nx, ny)
            if is_valid(nx, ny, grid):
                new_g = g_cost[current] + 1
                if next_pos not in g_cost or new_g < g_cost[next_pos]:
                    g_cost[next_pos] = new_g
                    f_cost = new_g + manhattan(next_pos, goal)
                    parent[next_pos] = current
                    heapq.heappush(heap, (f_cost, new_g, next_pos))

    return None, visited, expanded_nodes
