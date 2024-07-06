from pygame import init, QUIT, KEYDOWN, K_ESCAPE
from pygame.display import set_caption, set_mode, update
from pygame.event import poll
from pygame.font import Font
from pygame.time import Clock

from config import settings

init()

screen = set_mode(settings.WINDOW_SIZE)
small_font = Font('assets/fonts/font.ttf', 24)
score_font = Font('assets/fonts/font.ttf', 96)

set_caption("pygame-pong")

clock = Clock()

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
        "0",
        True,
        settings.WHITE
    )
    player_1_score_rect = player_1_score.get_rect(center=(350, 96))
    screen.blit(player_1_score, player_1_score_rect)

    player_2_score = score_font.render(
        "0",
        True,
        settings.WHITE
    )
    player_2_score_rect = player_2_score.get_rect(
        center=(settings.WINDOW_WIDTH - 350, 96)
    )
    screen.blit(player_2_score, player_2_score_rect)

    update()
