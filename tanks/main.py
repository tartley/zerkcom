import sys

import pyglet

from .options import create_parser
from .game import start
from .render import clear_screen
from .window import create_window


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    window = create_window(options)
    world = set()
    start(world)

    @window.event
    def on_draw():
        clear_screen()

    def update(dt):
        if options.exit:
            pyglet.app.exit()

        window.invalid = True

    pyglet.clock.schedule(update)
    window.invalid = False
    pyglet.app.run()


if __name__ == '__main__':
    main()

