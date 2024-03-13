from pygame import Rect, draw
from config import settings


class Player:
    def __init__(self, pad_position):
        self.score = 0

        if pad_position == 'left':
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

    def move_pad(self, dt, direction):
        if direction == 'up':
            self.pad.y -= settings.INITIAL_PAD_VELOCITY * dt
            if self.pad.top <= settings.PAD_GAP:
                self.pad.top = settings.PAD_GAP
        else:
            self.pad.y += settings.INITIAL_PAD_VELOCITY * dt
            if self.pad.bottom >= settings.WINDOW_HEIGHT - settings.PAD_GAP:
                self.pad.bottom = settings.WINDOW_HEIGHT - settings.PAD_GAP

    def add_points(self, points):
        self.score += points

    def draw_pad(self, surface, color):
        draw.rect(surface, color, self.pad)
