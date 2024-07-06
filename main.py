from pygame import init
from pygame.display import set_caption, set_mode
from pygame.time import Clock

from config import settings

init()

screen = set_mode(settings.WINDOW_SIZE)

set_caption("pygame-pong")

clock = Clock()

while True:
    dt = clock.tick(30)
