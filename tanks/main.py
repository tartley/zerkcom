import sys

import pyglet
from py2d.Math import Vector

from .view import render
from .options import create_parser
from .model.world import World
from .model.item import Item
from .resource import load_images


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
        position=Vector(100, 20),
        angle=-1.0,
    )


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    images = load_images('data/images')
    world = World()
    window = create_window(options)
    draw_sprites = render.init(window, world, images)
    player = create_player()
    world.add(player)

    @window.event
    def on_draw():
        draw_sprites((item, item.position, item.angle) for item in world)

    def update(dt):
        window.invalid = True
        player.angle += 0.002

    pyglet.clock.schedule(update)
    pyglet.app.run()

