from pygame import Rect
from pygame.draw import rect
from config import settings


class Player:
    def __init__(self, player_name):
        self.score = 0

        if player_name == settings.PLAYER_1:
            self.pad = Rect(
                settings.PAD_GAP,
                (settings.WINDOW_HEIGHT / 2) - (settings.PAD_HEIGHT / 2),
                settings.PAD_WIDTH,
                settings.PAD_HEIGHT
            )
        else:
            self.pad = Rect(
                settings.WINDOW_WIDTH - settings.PAD_WIDTH - settings.PAD_GAP,
                (settings.WINDOW_HEIGHT / 2) - (settings.PAD_HEIGHT / 2),
                settings.PAD_WIDTH,
                settings.PAD_HEIGHT,
            )

    def draw_pad(self, surface, color):
        rect(surface, color, self.pad)
