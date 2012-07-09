
from . import player
from . import wall


def start(world):
    for _ in range(10):
        world.add(wall.create())
    world.add(player.create())

