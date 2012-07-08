import sys

import pyglet

from .control import controllers
from .control.player import create_player
from .model.world import World
from .options import create_parser
from .view import window


# "setup.py install/develop" creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    world = World()
    win = window.init(world, options)
    controllers.init(win, world)
    world.add(create_player())
    pyglet.app.run()

