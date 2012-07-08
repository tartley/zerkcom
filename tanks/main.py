import sys

import pyglet

from . import keyhandlers
from .model.world import World
from .options import create_parser
from .control.player import create_player
from .resource import load_images
from .view import render


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
    world = World()
    window = create_window(options)
    draw_sprites = render.init(window, world, load_images('data/images'))
    keyhandlers.init(window, world)
    world.add(create_player())

    @window.event
    def on_draw():
        draw_sprites((item, item.position, item.angle) for item in world)

    def update(dt):
        for item in world:
            item.update(item, dt)
        window.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()

