import sys

import pyglet

from .options import create_parser


def create_window(options):
    return pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=True,
        resizable=True,
        caption='Adventure',
    )


# setup.py install/develop creates an executable that calls 'main()'
def main(*args):
    options = create_parser().parse_args(sys.argv[1:])
    window = create_window(options)

    @window.event
    def on_draw():
        window.clear()

    def update(dt):
        if options.exit:
            pyglet.app.exit()

        window.invalid = True

    pyglet.clock.schedule(update)
    window.invalid = False
    try:
        pyglet.app.run()
    finally:
        window.close()

