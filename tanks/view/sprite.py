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

    world.item_added += on_item_added

    def draw_sprites():
        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST) 
        gl.glTexParameteri(
            gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST) 

        for item in world:
            if hasattr(item, 'sprite'):
                item.sprite.x = item.position.x
                item.sprite.y = item.position.y
                item.sprite.rot = item.angle * RADIANS_TO_DEGREES
                item.sprite.render()

    return draw_sprites

