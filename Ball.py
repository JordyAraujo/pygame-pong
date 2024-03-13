from pygame import Rect, draw
import random

SIZE = 20
INITIAL_VELOCITY_X = 0.25
RANDOM_VELOCITY_Y = random.randrange(-5, 6) / 10


class Ball(Rect):
    def __init__(self, WINDOW_SIZE):
        super().__init__(0, 0, SIZE, SIZE)
        self.WINDOW_WIDTH = WINDOW_SIZE[0]
        self.WINDOW_HEIGHT = WINDOW_SIZE[1]

        self.SCREEN_X_CENTER = self.WINDOW_WIDTH / 2
        self.SCREEN_Y_CENTER = self.WINDOW_HEIGHT / 2
        self.center = (self.SCREEN_X_CENTER, self.SCREEN_Y_CENTER)

        self.velocity_x = INITIAL_VELOCITY_X
        self.velocity_y = RANDOM_VELOCITY_Y

    def move(self, dt):
        self.move_ip(self.velocity_x * dt, self.velocity_y * dt)

        if self.top <= 0 or self.bottom >= self.WINDOW_HEIGHT:
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
        self.velocity_x = INITIAL_VELOCITY_X
        self.velocity_y = RANDOM_VELOCITY_Y

        self.center = self.center = (
            self.SCREEN_X_CENTER,
            self.SCREEN_Y_CENTER
        )

    def draw(self, surface, color):
        draw.rect(surface, color, self)
