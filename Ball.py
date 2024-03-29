from pygame import Rect, draw
from config import settings


class Ball(Rect):
    def __init__(self):
        super().__init__(0, 0, settings.BALL_SIZE, settings.BALL_SIZE)

        self.center = (settings.SCREEN_X_CENTER, settings.SCREEN_Y_CENTER)

        self.velocity_x = settings.BALL_INITIAL_VELOCITY_X
        self.velocity_y = settings.BALL_RANDOM_VELOCITY_Y

    def move(self, dt):
        self.move_ip(self.velocity_x * dt, self.velocity_y * dt)

        if self.top <= 0 or self.bottom >= settings.WINDOW_HEIGHT:
            self.bounce_wall()

    def bounce_right(self, left_pad):
        self.velocity_x *= -1
        self.left = left_pad.right

    def bounce_left(self, right_pad):
        self.velocity_x *= -1
        self.right = right_pad.left

    def bounce_wall(self):
        self.velocity_y *= -1

    def reset(self):
        self.velocity_x = settings.BALL_INITIAL_VELOCITY_X
        self.velocity_y = settings.BALL_RANDOM_VELOCITY_Y

        self.center = self.center = (
            settings.SCREEN_X_CENTER,
            settings.SCREEN_Y_CENTER
        )

    def draw(self, surface, color):
        draw.rect(surface, color, self)
