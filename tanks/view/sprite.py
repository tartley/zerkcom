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
        if hasattr(item, 'image'):
            item.sprite = get_sprite(item.image, images[item.image])

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
            item.sprite.x = position.x
            item.sprite.y = position.y
            item.sprite.rot = angle * RADIANS_TO_DEGREES
            item.sprite.render()

    return draw_sprites

