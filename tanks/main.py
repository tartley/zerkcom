import sys

import pyglet

from .control import update, level
from .model.world import World
from .options import create_parser
from .view import window


# "setup.py install/develop" creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    world = World()
    win = window.init(world, options)
    update.init(win, world)
    level.start(world)
    pyglet.app.run()

