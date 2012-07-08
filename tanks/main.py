import sys

import pyglet

from . import keyhandlers
from .model.world import World
from .options import create_parser
from .control.player import create_player
from .resource import load_images
from .view import render, window


# setup.py install/develop creates an executable that calls 'main()'
def main():
    options = create_parser().parse_args(sys.argv[1:])
    world = World()
    win = window.create(options)
    draw_sprites = render.init(win, world, load_images('data/images'))
    keyhandlers.init(win, world)
    world.add(create_player())

    @win.event
    def on_draw():
        window.clear()
        draw_sprites((item, item.position, item.angle) for item in world)

    def update(dt):
        for item in world:
            item.update(item, dt)
        win.invalid = True

    pyglet.clock.schedule(update)
    pyglet.app.run()

