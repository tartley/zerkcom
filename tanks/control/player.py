from pyglet.window import key

from ..model.item import Item
from . import tank


def _tread_controls(keys):
    left = 0
    if keys[key.Q]:
        left += 1
    if keys[key.A]:
        left -= 1
    right = 0
    if keys[key.W]:
        right += 1
    if keys[key.S]:
        right -= 1
    return tank.Inputs(left, right)



def update(item, dt):
    tank.update(item, _tread_controls(item.keys), dt)


def create():
    return Item(
        image='tank',
        keys=key.KeyStateHandler(),
        update=update,
    )

