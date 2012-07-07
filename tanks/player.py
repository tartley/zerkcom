from math import sin, cos

from pyglet.window import key
from py2d.Math import Vector

from .model.item import Item




def create_player(window):

    keys = key.KeyStateHandler()
    window.push_handlers(keys)

    def player_keys(item, dt):
        if keys[key.UP]:
            item.position += Vector(-sin(item.angle), cos(item.angle)) * 3
        elif keys[key.DOWN]:
            item.position -= Vector(-sin(item.angle), cos(item.angle)) * 3
        if keys[key.LEFT]:
            item.angle += 0.06
        elif keys[key.RIGHT]:
            item.angle -= 0.06


    return Item(
        sprite='tank',
        position=Vector(100, 20),
        angle=-1.0,
        control=player_keys,
    )

