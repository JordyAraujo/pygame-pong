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
        self.bounced = False

    def move(self, dt):
        self.move_ip(self.velocity_x * dt, self.velocity_y * dt)

        if self.top <= 0 or self.bottom >= settings.WINDOW_HEIGHT:
            self.bounce_wall()

    def did_bounce(self):
        if self.bounced:
            self.bounced = False
            return True
        return False

    def bounce_right(self, left_pad):
        self.velocity_x *= -1
        self.left = left_pad.right

    def bounce_left(self, right_pad):
        self.velocity_x *= -1
        self.right = right_pad.left

    def bounce_wall(self):
        self.velocity_y *= -1
        self.bounced = True

    def reset(self):
        self.velocity_x = 0
        self.velocity_y = 0

        self.center = self.center = (
            settings.SCREEN_X_CENTER,
            settings.SCREEN_Y_CENTER
        )

    def serve(self):
        self.velocity_x = settings.BALL_INITIAL_VELOCITY_X
        self.velocity_y = settings.BALL_RANDOM_VELOCITY_Y

    def draw(self, surface, color):
        rect(surface, color, self)
