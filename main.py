from pygame import (
    init,
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_w,
    K_s,
    K_UP,
    K_DOWN,
    K_KP_ENTER,
    K_SPACE,
    K_RETURN
)
from pygame.display import set_caption, set_mode, update
from pygame.event import poll
from pygame.font import Font
from pygame.key import get_pressed
from pygame.mixer import init as mixer_init, Sound, pre_init
from pygame.time import Clock

from Ball import Ball
from Player import Player

from config import settings

pre_init(44100, -8, 1, 8)
mixer_init()
init()

screen = set_mode(settings.WINDOW_SIZE)
small_font = Font('assets/fonts/font.ttf', 24)
score_font = Font('assets/fonts/font.ttf', 96)

game_start_sound = Sound('assets/sounds/game_start.wav')
player_hit_sound = Sound('assets/sounds/player_hit.wav')
wall_hit_sound = Sound('assets/sounds/wall_hit.wav')
score_sound = Sound('assets/sounds/score.wav')

set_caption("pygame-pong")

clock = Clock()

ball = Ball()

player_1 = Player(settings.PLAYER_1)
player_2 = Player(settings.PLAYER_2)

# The state of our game; can be any of the following:
# 1. 'start' (the beginning of the game, before first serve)
# 2. 'serve' (waiting on a key press to serve the ball)
# 3. 'play' (the ball is in play, bouncing between paddles)
# 4. 'done' (the game is over, with a victor, ready for restart)
game_state = 'start'
Sound.play(game_start_sound)

while True:
    dt = clock.tick(30)

    game_event = poll()

    if (
        game_event.type == QUIT
        or game_event.type == KEYDOWN
        and game_event.key == K_ESCAPE
    ):
        break

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

    if game_state == 'start':        
        # reset_game()
        text = small_font.render(
            "Press SPACE or ENTER to start",
            True,
            settings.WHITE
        )
        text_rect = text.get_rect(center=(settings.WINDOW_WIDTH / 2, 200))
        screen.blit(text, text_rect)
        if (
            game_event.type == KEYDOWN and
            (
                game_event.key == K_SPACE or
                game_event.key == K_KP_ENTER or
                game_event.key == K_RETURN
            )
        ):
            Sound.play(score_sound)
            game_state = 'serve'
    elif game_state == 'serve':
        text = small_font.render(
            "Press SPACE or ENTER to serve",
            True,
            settings.WHITE
        )
        text_rect = text.get_rect(center=(settings.WINDOW_WIDTH / 2, 200))
        screen.blit(text, text_rect)
        if (
            game_event.type == KEYDOWN and
            (
                game_event.key == K_SPACE or
                game_event.key == K_KP_ENTER or
                game_event.key == K_RETURN
            )
        ):
            Sound.play(score_sound)
            ball.serve()
            game_state = 'play'
    elif game_state == 'play':
        pressed = get_pressed()
        if pressed[K_w]:
            player_1.move_pad(dt, 'up')
        if pressed[K_s]:
            player_1.move_pad(dt, 'down')
        if pressed[K_UP]:
            player_2.move_pad(dt, 'up')
        if pressed[K_DOWN]:
            player_2.move_pad(dt, 'down')

        ball.move(dt)
        if ball.did_bounce():
            Sound.play(wall_hit_sound)

        if ball.colliderect(player_1.pad):
            Sound.play(player_hit_sound)
            ball.bounce_right(player_1.pad)

        if ball.colliderect(player_2.pad):
            Sound.play(player_hit_sound)
            ball.bounce_left(player_2.pad)

        if ball.left <= 0:
            player_2.add_points(1)
            if player_2.score == settings.WINNING_SCORE:
                Sound.play(game_start_sound)
                game_state = 'done'
            Sound.play(score_sound)
            ball.reset()
            game_state = 'serve'

        if ball.right >= settings.WINDOW_WIDTH:
            player_1.add_points(1)
            if player_1.score == settings.WINNING_SCORE:
                Sound.play(game_start_sound)
                game_state = 'done'
            Sound.play(score_sound)
            ball.reset()
            game_state = 'serve'
    elif game_state == 'done':
        text = small_font.render(
            "Game Over! Press SPACE or ENTER to restart",
            True,
            settings.WHITE
        )
        text_rect = text.get_rect(center=(settings.WINDOW_WIDTH / 2, 200))
        screen.blit(text, text_rect)
        if (
            game_event.type == KEYDOWN and
            (
                game_event.key == K_SPACE or
                game_event.key == K_KP_ENTER or
                game_event.key == K_RETURN
            )
        ):
            game_state = 'start'

    ball.draw(screen, settings.WHITE)

    for player in [player_1, player_2]:
        player.draw_pad(screen, settings.WHITE)

    update()
