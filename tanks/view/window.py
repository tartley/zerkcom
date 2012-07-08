import pyglet
from pyglet import gl

from ..image import load_all
from . import sprite


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

    draw_sprites = sprite.init(window, world, load_all('data/images'))

    return window

