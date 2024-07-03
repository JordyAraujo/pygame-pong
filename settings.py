from time import time
import random

random.seed(time())

# Players
PLAYER_1 = 'left'
PLAYER_2 = 'right'

# Colors
BACKGROUND = (40, 45, 52)
WHITE = (255, 255, 255)

# Window settings
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Screen settings
SCREEN_X_CENTER = WINDOW_WIDTH / 2
SCREEN_Y_CENTER = WINDOW_HEIGHT / 2
SCREEN_CENTER = (SCREEN_X_CENTER, SCREEN_Y_CENTER)

# Ball settings
BALL_SIZE = 20
BALL_INITIAL_VELOCITY_X = 0.25
BALL_RANDOM_VELOCITY_Y = random.randrange(-5, 6) / 10

# Player settings
INITIAL_PAD_VELOCITY = 0.5
PAD_WIDTH = 20
PAD_HEIGHT = 90
PAD_GAP = 10
