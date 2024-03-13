from time import time as seed_time
from pygame import (
    init,
    display,
    font,
    event,
    key,
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_w,
    K_s,
    K_UP,
    K_DOWN,
    time as time
)
import random
from Ball import Ball
from Player import Player

BACKGROUND = (40, 45, 52)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

SCREEN_X_CENTER = WINDOW_WIDTH / 2
SCREEN_Y_CENTER = WINDOW_HEIGHT / 2
SCREEN_CENTER = (SCREEN_X_CENTER, SCREEN_Y_CENTER)

init()
random.seed(seed_time())

screen = display.set_mode(WINDOW_SIZE)
small_font = font.Font('assets/fonts/font.ttf', 24)
score_font = font.Font('assets/fonts/font.ttf', 96)

display.set_caption("pygame-pong")

clock = time.Clock()

ball = Ball(WINDOW_SIZE)

player_1 = Player('left', WINDOW_SIZE)
player_2 = Player('right', WINDOW_SIZE)

while True:
    dt = clock.tick(30)

    pygame_event = event.poll()

    if (
        pygame_event.type == QUIT
        or pygame_event.type == KEYDOWN
        and pygame_event.key == K_ESCAPE
    ):
        break

    pressed = key.get_pressed()
    if pressed[K_w]:
        player_1.move(dt, 'up')
    if pressed[K_s]:
        player_1.move(dt, 'down')
    if pressed[K_UP]:
        player_2.move(dt, 'up')
    if pressed[K_DOWN]:
        player_2.move(dt, 'down')

    screen.fill(BACKGROUND)

    text = small_font.render("Hello Pong!", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 24))
    screen.blit(text, text_rect)

    player_1_score = score_font.render(str(player_1.score), True, WHITE)
    player_1_score_rect = player_1_score.get_rect(center=(350, 96))
    screen.blit(player_1_score, player_1_score_rect)

    player_2_score = score_font.render(str(player_2.score), True, WHITE)
    player_2_score_rect = player_2_score.get_rect(
        center=(WINDOW_WIDTH - 350, 96)
    )
    screen.blit(player_2_score, player_2_score_rect)

    ball.move(dt)

    if ball.colliderect(player_1.pad):
        ball.bounce_right(player_1.pad)

    if ball.colliderect(player_2.pad):
        ball.bounce_left(player_2.pad)

    if ball.left <= 0:
        player_2.score += 1
        ball.reset()

    if ball.right >= WINDOW_WIDTH:
        player_1.score += 1
        ball.reset()

    ball.draw(screen, WHITE)

    for player in [player_1, player_2]:
        player.draw_pad(screen, WHITE)

    display.flip()
