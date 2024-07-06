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

        self.velocity_x = settings.BALL_INITIAL_VELOCITY_X
        self.velocity_y = settings.BALL_RANDOM_VELOCITY_Y

    def move(self, dt):
        self.move_ip(self.velocity_x * dt, self.velocity_y * dt)

    def draw(self, surface, color):
        rect(surface, color, self)
