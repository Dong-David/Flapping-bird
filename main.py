# main.py
import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Cấu hình màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Flappy Bird")

# Clock để giới hạn FPS
clock = pygame.time.Clock()
FPS = 60

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật game (logic sẽ đặt ở đây)

    # Vẽ
    screen.fill((30, 30, 30))  # màu nền xám tối
    pygame.display.flip()

    # Giới hạn FPS
    clock.tick(FPS)

# Thoát pygame
pygame.quit()
sys.exit()
