import random

from . import player
from . import wall


def start(world):
    for _ in range(10):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        width = random.randint(20, 200)
        height = 20
        if random.randint(0, 1):
            width, height = height, width
        world.add(wall.create(x, y, x + width, y + height))
    world.add(player.create())

