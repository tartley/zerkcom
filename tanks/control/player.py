from py2d.Math import Vector
from pyglet.window import key

from ..model.item import Item
from .tank import update_tank


def player_control(item, dt):
    item.speed_left = 0
    if item.keys[key.Q]:
        item.speed_left += 1
    if item.keys[key.A]:
        item.speed_left -= 1

    item.speed_right = 0
    if item.keys[key.P]:
        item.speed_right += 1
    if item.keys[key.L]:
        item.speed_right -= 1
    
    update_tank(item, dt)


def create():
    return Item(
        image='tank',
        position=Vector(-300, 0),
        angle=0.0,
        keys=key.KeyStateHandler(),
        update=player_control,
    )

