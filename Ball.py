from pygame import Rect, draw
import random

INITIAL_VELOCITY_X = 0.25
RANDOM_VELOCITY_Y = random.randrange(-5, 6) / 10


class Ball(Rect):
    def __init__(self, size, SCREEN_CENTER):
        super().__init__(0, 0, size, size)
        self.center = SCREEN_CENTER
        self.velocity_x = INITIAL_VELOCITY_X
        self.velocity_y = RANDOM_VELOCITY_Y

    def move(self, dt):
        self.move_ip(self.velocity_x * dt, self.velocity_y * dt)

    def bounce_right(self, left_pad):
        self.velocity_x *= -1
        self.left = left_pad.right

    def bounce_left(self, right_pad):
        self.velocity_x *= -1
        self.right = right_pad.left

    def bounce_wall(self):
        self.velocity_y *= -1

    def reset(self, SCREEN_CENTER):
        self.velocity_x = INITIAL_VELOCITY_X
        self.velocity_y = RANDOM_VELOCITY_Y
        self.center = SCREEN_CENTER

    def draw(self, surface, color):
        draw.rect(surface, color, self)
