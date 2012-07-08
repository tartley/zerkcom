import pyglet
import rabbyt

from ..image import load_all
from . import sprite


CLEAR_COLOR_DEFAULT = (0.1, 0.3, 0.2)


def clear(color=CLEAR_COLOR_DEFAULT):
    rabbyt.clear(rgba=CLEAR_COLOR_DEFAULT)


def init(world, options):

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )

    rabbyt.set_viewport((window.width, window.height))
    rabbyt.set_default_attribs()

    @window.event
    def on_draw():
        clear()
        draw_sprites((item, item.position, item.angle) for item in world)

    draw_sprites = sprite.init(window, world, load_all('data/images'))

    return window

