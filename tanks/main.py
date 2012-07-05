import sys

import pyglet

from .view import render
from .options import create_parser
from .model.world import World
from .model.item import Item


def create_window(options):
    return pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )



def create_player():
    return Item(
        sprite='tank',
    )


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    window = create_window(options)
    world = World()
    render.init(window, world)

    world.add(create_player())

    def update(dt):
        window.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()


if __name__ == '__main__':
    main()

