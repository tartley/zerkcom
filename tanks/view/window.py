import pyglet
from pyglet import gl

from ..resource import load_images
from . import render


CLEAR_COLOR_DEFAULT = (0.1, 0.2, 0.3, 1.0)


def clear(color=CLEAR_COLOR_DEFAULT):
    r, g, b, _ = color
    gl.glClearColor(r, g, b, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)


def init(world, options):

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )

    @window.event
    def on_draw():
        clear()
        draw_sprites((item, item.position, item.angle) for item in world)

    draw_sprites = render.init(window, world, load_images('data/images'))

    return window

