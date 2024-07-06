from pygame import Rect
from pygame.draw import rect
from config import settings


class Ball(Rect):
    def __init__(self):
        super().__init__(
            settings.SCREEN_X_CENTER,
            settings.SCREEN_Y_CENTER,
            settings.BALL_SIZE,
            settings.BALL_SIZE
        )

    def draw(self, surface, color):
        rect(surface, color, self)
