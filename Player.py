from pygame import Rect, draw

INITIAL_PAD_VELOCITY = 0.5
PAD_WIDTH = 20
PAD_HEIGHT = 90
PAD_SCREEN_GAP = 10


class Player:
    def __init__(self, pad_position, WINDOW_SIZE):
        self.score = 0

        self.WINDOW_WIDTH = WINDOW_SIZE[0]
        self.WINDOW_HEIGHT = WINDOW_SIZE[1]

        if pad_position == 'left':
            self.pad = Rect(
                PAD_SCREEN_GAP,
                (self.WINDOW_HEIGHT / 2) - (PAD_HEIGHT / 2),
                PAD_WIDTH,
                PAD_HEIGHT
            )
        else:
            self.pad = Rect(
                self.WINDOW_WIDTH - PAD_WIDTH - PAD_SCREEN_GAP,
                (self.WINDOW_HEIGHT / 2) - (PAD_HEIGHT / 2),
                PAD_WIDTH,
                PAD_HEIGHT,
            )

    def move(self, dt, direction):
        if direction == 'up':
            self.pad.y -= INITIAL_PAD_VELOCITY * dt
            if self.pad.top <= PAD_SCREEN_GAP:
                self.pad.top = PAD_SCREEN_GAP
        else:
            self.pad.y += INITIAL_PAD_VELOCITY * dt
            if self.pad.bottom >= self.WINDOW_HEIGHT - PAD_SCREEN_GAP:
                self.pad.bottom = self.WINDOW_HEIGHT - PAD_SCREEN_GAP

    def draw_pad(self, surface, color):
        draw.rect(surface, color, self.pad)
