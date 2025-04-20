# ucs.py - Uniform Cost Search (UCS)
# Ghost: Orange

import heapq
from utils import is_valid, reconstruct_path

# Di chuyển 4 hướng (chi phí mặc định là 1)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def ucs(grid, start, goal):
    heap = [(0, start)]  # (cost, position)
    visited = set()
    parent = {}
    cost_so_far = {start: 0}
    expanded_nodes = 0

    while heap:
        cost, current = heapq.heappop(heap)
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
                new_cost = cost_so_far[current] + 1  # chi phí = 1 cho mỗi bước
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    parent[next_pos] = current
                    heapq.heappush(heap, (new_cost, next_pos))

    return None, visited, expanded_nodes
