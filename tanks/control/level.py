import random

from . import player
from . import wall


def start(world):
    #for _ in range(10):
        #x = random.randint(-400, 400)
        #y = random.randint(-400, 400)
        #width = random.randint(10, 200)
        #height = 10
        #if random.randint(0, 1):
            #width, height = height, width
        #world.add(wall.create(x, y, x + width, y + height))
    world.add(wall.create(-200, -100, +200, -80))
    world.add(player.create())

