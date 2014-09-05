from __future__ import division

import pyglet
import rabbyt

from ..image import load_all
from . import sprite
from . import glyph


CLEAR_COLOR_DEFAULT = (0.1, 0.3, 0.2)
WORLD_BOUNDS = (-24 * 16, -14 * 16, 24 * 16, 14 * 16)
VIEWPORT_ASPECT = 48 / 30
HUD_SIZE = 2 / 30


def get_viewport(win_width, win_height):
    win_aspect = win_width / win_height
    width, height = win_width, win_height
    if win_aspect < VIEWPORT_ASPECT:
        # window is too tall
        height *= win_aspect / VIEWPORT_ASPECT
    else:
        # window is too wide
        width /= win_aspect / VIEWPORT_ASPECT

    hud_height = height * HUD_SIZE

    return (
        (win_width - width) / 2, (win_height - height) / 2,
        (win_width + width) / 2, (win_height + height) / 2 - hud_height
    )


def init(world, options):

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Zerkcom',
    )

    rabbyt.set_default_attribs()

    draw_glyphs = glyph.init(window, world)
    draw_sprites = sprite.init(window, world, load_all('data/images'))

    @window.event
    def on_draw():
        rabbyt.clear(rgba=CLEAR_COLOR_DEFAULT)
        rabbyt.set_viewport(
            get_viewport(window.width, window.height),
            WORLD_BOUNDS
        )
        draw_glyphs()
        draw_sprites()

    return window

