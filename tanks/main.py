import sys

import pyglet

from .options import create_parser
from .view.render import clear_screen
from .model.world import World


def create_window(options):
    return pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    window = create_window(options)
    world = World()

    @window.event
    def on_draw():
        clear_screen()

    def update(dt):
        window.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()


if __name__ == '__main__':
    main()

