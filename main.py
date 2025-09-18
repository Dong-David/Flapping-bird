import pygame, sys, random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 288, 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Flappy Bird")

# Background
background = pygame.image.load("assets/sprites/background-day.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Message
message = pygame.image.load("assets/sprites/message.png").convert_alpha()
msg_rect = message.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

# Score
score = pygame.image.load("assets/sprites/0.png").convert_alpha()

# Pipe image
pipe_img = pygame.image.load("assets/sprites/pipe-green.png").convert_alpha()

clock = pygame.time.Clock()
FPS = 60

# Biến alpha toàn cục
alpha = 0
delta = 3

PIPE_HEIGHT = 320
GAP = 100


class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randint(50, SCREEN_HEIGHT - 50 - GAP)

    def moving(self):
        self.x -= 2

    def draw(self):
        screen.blit(pipe_img, (self.x, self.y))


# Danh sách pipes
pipes = []
pipes.append(Pipe())


def waiting():
    global alpha, delta
    alpha += delta
    if alpha >= 255 or alpha <= 0:
        delta = -delta

    msg_temp = message.copy()
    msg_temp.set_alpha(alpha)
    screen.blit(msg_temp, msg_rect)


def startGame():
    # Cập nhật pipes
    for p in pipes:
        p.moving()
        p.draw()

    # Vẽ score tạm
    screen.blit(score, (SCREEN_WIDTH // 2 - 12, 50))


def main():
    running = True
    state = "waiting"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = "startGame"

        # Vẽ background trước
        screen.blit(background, (0, 0))

        # Vẽ theo state
        if state == "waiting":
            waiting()
        elif state == "startGame":
            startGame()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
