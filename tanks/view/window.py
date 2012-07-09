import pyglet
import rabbyt

from ..image import load_all
from . import sprite
from . import glyph


CLEAR_COLOR_DEFAULT = (0.1, 0.3, 0.2)


def init(world, options):

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )

    rabbyt.set_default_attribs()

    draw_glyphs = glyph.init(window, world)
    draw_sprites = sprite.init(window, world, load_all('data/images'))

    @window.event
    def on_draw():
        rabbyt.clear(rgba=CLEAR_COLOR_DEFAULT)
        rabbyt.set_viewport((window.width, window.height), (800, 600))
        draw_glyphs()
        draw_sprites()

    return window

