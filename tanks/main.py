import sys

import pyglet

from . import keyhandlers
from .model.world import World
from .options import create_parser
from .control.player import create_player
from .view import window


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    world = World()
    win = window.init(world, options)

    keyhandlers.init(win, world)
    world.add(create_player())

    def update(dt):
        for item in world:
            item.update(item, dt)
        win.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()

