# utils.py - chứa các hàm hỗ trợ chung

import time
import tracemalloc

def is_valid(x, y, grid):
    """
    Kiểm tra ô (x, y) có hợp lệ để đi qua hay không
    - Trong phạm vi bản đồ
    - Không phải là tường
    """
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == '0'


def measure_performance(func, *args):
    """
    Đo hiệu suất chạy của hàm tìm kiếm:
    - thời gian chạy
    - bộ nhớ tiêu thụ
    """
    tracemalloc.start()
    start_time = time.time()

    result = func(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end_time - start_time, peak / 1024  # KB


def reconstruct_path(parent, start, goal):
    """
    Truy vết đường đi từ điểm đích về điểm xuất phát
    bằng dictionary parent lưu trước đó.
    """
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path


def load_map_from_file(file_path):
    """
    Đọc bản đồ từ file .txt:
    - '0': đường đi
    - '1': tường
    - 'G': Ghost (lấy vị trí đầu tiên tìm thấy)
    - 'P': Pac-Man
    - Trả về: lưới, vị trí Pac-Man, vị trí Ghost, danh sách thức ăn (rỗng nếu không dùng)
    """
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    grid = []
    pacman_pos = None
    ghost_positions = []
    food_positions = []

    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            row.append('0' if char in ['0', 'P', 'G'] else '1')  # Đường đi hoặc tường
            if char == 'P':
                pacman_pos = (x, y)
            elif char == 'G':
                ghost_positions.append((x, y))
            elif char == '.':
                food_positions.append((x, y))
        grid.append(row)

    if pacman_pos is None or not ghost_positions:
        raise ValueError("Map must contain (P) or (G).")

    return grid, pacman_pos, ghost_positions, food_positions

