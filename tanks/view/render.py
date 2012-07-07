import math

import pyglet
from pyglet import gl


CLEAR_COLOR_DEFAULT = (0.1, 0.2, 0.3, 1.0)
RADIANS_TO_DEGREES = 360.0 / (math.pi * 2)


def clear_screen(color=CLEAR_COLOR_DEFAULT):
    r, g, b, _ = color
    gl.glClearColor(r, g, b, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

def get_sprite(name, image):
    sprite = pyglet.sprite.Sprite(image)
    sprite.scale = 4
    return sprite


def init(window, world, images):

    def on_item_added(item):
        item._sprite = get_sprite(item.sprite, images[item.sprite])

    def on_item_removed(item):
        pass

    world.item_added += on_item_added
    world.item_removed += on_item_removed

    def draw_sprites(items):
        clear_screen()

        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST) 
        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST) 

        for item, position, angle in items:
            item._sprite.set_position(position.x, position.y)
            item._sprite.rotation = angle * RADIANS_TO_DEGREES
            item._sprite.draw()

    return draw_sprites

