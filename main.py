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
    draw,
    Rect,
    time as time
)
import random
from Ball import Ball

BACKGROUND = (40, 45, 52)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SCREEN_CENTER = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

init()
random.seed(seed_time())

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
small_font = font.Font('assets/fonts/font.ttf', 24)
score_font = font.Font('assets/fonts/font.ttf', 96)

display.set_caption("pygame-pong")

PAD_VELOCITY = 0.5

clock = time.Clock()

player_1_points = 0
player_2_points = 0

PADS_WIDTH = 20
PADS_HEIGHT = 90
BALL_SIZE = 20

ball = Ball(BALL_SIZE, SCREEN_CENTER)

left_pad = Rect(
    10,
    (WINDOW_HEIGHT / 2) - (PADS_HEIGHT / 2),
    PADS_WIDTH,
    PADS_HEIGHT
)

right_pad = Rect(
    WINDOW_WIDTH - PADS_WIDTH - 10,
    (WINDOW_HEIGHT / 2) - (PADS_HEIGHT / 2),
    PADS_WIDTH,
    PADS_HEIGHT,
)

pads = [left_pad, right_pad]

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
        left_pad.move_ip(0, -PAD_VELOCITY * dt)
    if pressed[K_s]:
        left_pad.move_ip(0, PAD_VELOCITY * dt)
    if pressed[K_UP]:
        right_pad.move_ip(0, -PAD_VELOCITY * dt)
    if pressed[K_DOWN]:
        right_pad.move_ip(0, PAD_VELOCITY * dt)

    screen.fill(BACKGROUND)

    text = small_font.render("Hello Pong!", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, 24))
    screen.blit(text, text_rect)

    player_1_score = score_font.render(str(player_1_points), True, WHITE)
    player_1_score_rect = player_1_score.get_rect(center=(350, 96))
    screen.blit(player_1_score, player_1_score_rect)

    player_2_score = score_font.render(str(player_2_points), True, WHITE)
    player_2_score_rect = player_2_score.get_rect(
        center=(WINDOW_WIDTH - 350, 96)
    )
    screen.blit(player_2_score, player_2_score_rect)

    ball.move(dt)

    if ball.colliderect(left_pad):
        ball.bounce_right(left_pad)

    if ball.colliderect(right_pad):
        ball.bounce_left(right_pad)

    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball.bounce_wall()

    if ball.left <= 0:
        player_2_points += 1
        ball.reset(SCREEN_CENTER)

    if ball.right >= WINDOW_WIDTH:
        player_1_points += 1
        ball.reset(SCREEN_CENTER)

    if left_pad.top <= 0:
        left_pad.top = 0

    if left_pad.bottom >= WINDOW_HEIGHT:
        left_pad.bottom = WINDOW_HEIGHT

    if right_pad.top <= 0:
        right_pad.top = 0

    if right_pad.bottom >= WINDOW_HEIGHT:
        right_pad.bottom = WINDOW_HEIGHT

    ball.draw(screen, WHITE)

    for pad in pads:
        draw.rect(screen, WHITE, pad)

    display.flip()
