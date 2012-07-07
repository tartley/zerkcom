import sys

import pyglet

from .view import render
from .options import create_parser
from .model.world import World
from .resource import load_images
from .player import create_player


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
    images = load_images('data/images')
    world = World()
    window = create_window(options)
    draw_sprites = render.init(window, world, images)
    player = create_player(window)
    world.add(player)

    @window.event
    def on_draw():
        draw_sprites((item, item.position, item.angle) for item in world)

    def update(dt):
        for item in world:
            item.control(item, dt)
        window.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()

