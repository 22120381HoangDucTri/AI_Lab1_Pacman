import pygame
import time

# Màu sắc RGB
COLOR_WALL = (40, 40, 40) # Xám đậm
COLOR_PATH = (200, 200, 200) # Xám nhạt
COLOR_VISITED = (170, 240, 180) # Xanh lá nhạt
COLOR_PACMAN = (255, 255, 0) # Vàng
COLOR_GHOST = (0, 100, 255) # Xanh dương
COLOR_ROUTE = (255, 100, 100) # Đỏ
CELL_SIZE = 32


def draw_grid(screen, grid, pacman_pos, ghost_pos, path=None, visited=None):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pos = (x, y)
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            char = grid[y][x]

            # Ưu tiên các thực thể
            if pos == pacman_pos:
                pygame.draw.rect(screen, COLOR_PACMAN, rect)
            elif pos == ghost_pos:
                pygame.draw.rect(screen, COLOR_GHOST, rect)
            elif path and pos in path:
                pygame.draw.rect(screen, COLOR_ROUTE, rect)
            elif visited and pos in visited:
                pygame.draw.rect(screen, COLOR_VISITED, rect)
            elif char == '1':
                pygame.draw.rect(screen, COLOR_WALL, rect)
            else:
                pygame.draw.rect(screen, COLOR_PATH, rect)

            pygame.draw.rect(screen, (0, 0, 0), rect, 1)


def visualize(window, grid, pacman_pos, ghost_pos, path, visited=None):
    pygame.init()

    width = len(grid[0]) * CELL_SIZE
    height = len(grid) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(window)

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((255, 255, 255))
        draw_grid(screen, grid, pacman_pos, ghost_pos, path, visited)
        pygame.display.flip()
        clock.tick(60)

        # Thoát bằng nút đóng cửa sổ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
