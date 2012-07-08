import math

from pyglet import gl
import rabbyt


RADIANS_TO_DEGREES = 360.0 / (math.pi * 2)


def get_sprite(name, image):
    sprite = rabbyt.Sprite(image)
    sprite.scale = 6
    return sprite


def init(window, world, images):

    def on_item_added(item):
        item._sprite = get_sprite(item.sprite, images[item.sprite])

    def on_item_removed(item):
        pass

    world.item_added += on_item_added
    world.item_removed += on_item_removed

    def draw_sprites(items):
        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST) 
        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST) 

        for item, position, angle in items:
            item._sprite.x = position.x
            item._sprite.y = position.y
            item._sprite.rot = angle * RADIANS_TO_DEGREES
            item._sprite.render()

    return draw_sprites

