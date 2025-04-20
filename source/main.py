import argparse
import os
from utils import load_map_from_file, measure_performance
from algorithms import bfs, dfs, ucs, astar
from visualizer import visualize


def run_algorithm(name, func, grid, start, goal):
    print(f"\n{name.upper()}:")
    (path, visited, expanded), time_taken, memory_kb = measure_performance(func, grid, start, goal)

    if path is None:
        print("Cannot find path.")
    else:
        print(f"Path's length: {len(path)} steps")
        print(f"Nodes expanded: {expanded}")
        print(f"Time: {time_taken:.6f} seconds")
        print(f"Memory: {memory_kb:.2f} KB")

    return {
        "name": name,
        "path": path,
        "visited": visited,
        "expanded": expanded,
        "time": time_taken,
        "memory": memory_kb
    }

def main():
    # Chỉ định map với cmd arg --map
    parser = argparse.ArgumentParser(description="Pac-Man AI - Multi-Ghost Search")
    parser.add_argument("--map", type=str, default="maps/map2.txt", help="Đường dẫn tới file bản đồ .txt")
    args = parser.parse_args()

    map_path = args.map

    # Load bản đồ và vị trí nhân vật
    grid, pacman_pos, ghost_positions, _ = load_map_from_file(map_path)

    # Kiểm tra có ghost không
    if not ghost_positions:
        print("Cannot find any ghost in the map.")
        return

    start = ghost_positions[0]  # Chọn ghost đầu tiên
    goal = pacman_pos           # Vị trí Pac-Man

    print(f"Ghost {start} -> Pacman {goal}")
    print(f"Map: {map_path}")

    # Đo hiệu suất và thực hiện thuật toán
    results = []
    results.append(run_algorithm("BFS", bfs.bfs, grid, start, goal))
    results.append(run_algorithm("DFS", dfs.dfs, grid, start, goal))
    results.append(run_algorithm("UCS", ucs.ucs, grid, start, goal))
    results.append(run_algorithm("A*", astar.astar, grid, start, goal))

    # Hiển thị kết quả trên GUI
    window_names = ["BFS", "DFS", "UCS", "A*"]
    for i in range(4):
        if results[i]["path"] is not None:
            print(f"\nShow: {results[i]['name'].upper()}")
            visualize(window_names[i], grid, goal, start, results[i]["path"], results[i]["visited"])
    

if __name__ == "__main__":
    main()
