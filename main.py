import pygame

BACKGROUND = (40, 45, 52)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
small_font = pygame.font.Font('assets/fonts/font.ttf', 24)

pygame.display.set_caption("pygame-pong")

PADS_WIDTH = 20
PADS_HEIGHT = 90
BALL_SIZE = 20

ball = pygame.Rect(
    (WINDOW_WIDTH / 2) - (BALL_SIZE / 2),
    (WINDOW_HEIGHT / 2) - (BALL_SIZE / 2),
    BALL_SIZE,
    BALL_SIZE,
)

left_pad = pygame.Rect(
    10,
    (WINDOW_HEIGHT / 2) - (PADS_HEIGHT / 2),
    PADS_WIDTH,
    PADS_HEIGHT
)

right_pad = pygame.Rect(
    WINDOW_WIDTH - PADS_WIDTH - 10,
    (WINDOW_HEIGHT / 2) - (PADS_HEIGHT / 2),
    PADS_WIDTH,
    PADS_HEIGHT,
)

pads = [left_pad, right_pad]

while True:

    event = pygame.event.poll()

    if (
        event.type == pygame.QUIT
        or event.type == pygame.KEYDOWN
        and event.key == pygame.K_ESCAPE
    ):
        break


    screen.fill(BACKGROUND)

    text = small_font.render("Hello Pong!", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 24))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, WHITE, ball)

    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.flip()
