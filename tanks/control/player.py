from py2d.Math import Vector
from pyglet.window import key

from ..model.item import Item
from .tank import update_tank


def keys(item, dt):
    item.speed_left = 0
    if item.keyhandler[key.Q]:
        item.speed_left += 1
    if item.keyhandler[key.A]:
        item.speed_left -= 1

    item.speed_right = 0
    if item.keyhandler[key.P]:
        item.speed_right += 1
    if item.keyhandler[key.L]:
        item.speed_right -= 1
    
    update_tank(item, dt)


def create():
    return Item(
        sprite='tank',
        position=Vector(100, 20),
        angle=-1.0,
        keyhandler=key.KeyStateHandler(),
        update=keys,
    )

