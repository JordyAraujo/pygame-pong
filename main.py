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
    time
)
from Ball import Ball
from Player import Player
from config import settings

init()

screen = display.set_mode(settings.WINDOW_SIZE)
small_font = font.Font('assets/fonts/font.ttf', 24)
score_font = font.Font('assets/fonts/font.ttf', 96)

display.set_caption("pygame-pong")

clock = time.Clock()

ball = Ball()

player_1 = Player('left')
player_2 = Player('right')

while True:
    dt = clock.tick(30)

    game_event = event.poll()

    if (
        game_event.type == QUIT
        or game_event.type == KEYDOWN
        and game_event.key == K_ESCAPE
    ):
        break

    pressed = key.get_pressed()
    if pressed[K_w]:
        player_1.move_pad(dt, 'up')
    if pressed[K_s]:
        player_1.move_pad(dt, 'down')
    if pressed[K_UP]:
        player_2.move_pad(dt, 'up')
    if pressed[K_DOWN]:
        player_2.move_pad(dt, 'down')

    screen.fill(settings.BACKGROUND)

    text = small_font.render("Pygame Pong!", True, settings.WHITE)
    text_rect = text.get_rect(center=(settings.WINDOW_WIDTH / 2, 24))
    screen.blit(text, text_rect)

    player_1_score = score_font.render(
        str(player_1.score),
        True,
        settings.WHITE
    )
    player_1_score_rect = player_1_score.get_rect(center=(350, 96))
    screen.blit(player_1_score, player_1_score_rect)

    player_2_score = score_font.render(
        str(player_2.score),
        True,
        settings.WHITE
    )
    player_2_score_rect = player_2_score.get_rect(
        center=(settings.WINDOW_WIDTH - 350, 96)
    )
    screen.blit(player_2_score, player_2_score_rect)

    ball.move(dt)

    if ball.colliderect(player_1.pad):
        ball.bounce_right(player_1.pad)

    if ball.colliderect(player_2.pad):
        ball.bounce_left(player_2.pad)

    if ball.left <= 0:
        player_2.add_points(1)
        ball.reset()

    if ball.right >= settings.WINDOW_WIDTH:
        player_1.add_points(1)
        ball.reset()

    ball.draw(screen, settings.WHITE)

    for player in [player_1, player_2]:
        player.draw_pad(screen, settings.WHITE)

    display.flip()
