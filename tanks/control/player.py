from pyglet.window import key

from ..model.item import Item
from . import tank


def _tread_controls(keys):
    left = 1 * keys[key.Q] - 1 * keys[key.A]
    right = 1 * keys[key.W] - 1 * keys[key.S]
    return tank.Inputs(left, right)


def _cursor_controls(keys):
    direction = 1 * keys[key.UP] - 1 * keys[key.DOWN]
    left = right = 0
    inner = -1 * (direction != +1)
    outer = +1 * (direction != -1)
    if keys[key.LEFT]:
        left += inner
        right += outer
    elif keys[key.RIGHT]:
        left += outer
        right += inner
    else:
        left = right = direction

    return tank.Inputs(left, right)


def _key_controls(keys):
    inputs = _tread_controls(keys)
    if inputs == (0, 0):
        inputs = _cursor_controls(keys)
    return inputs


def update(item, dt):
    tank.update(item, _key_controls(item.keys), dt)


def create():
    return Item(
        image='tank',
        keys=key.KeyStateHandler(),
        update=update,
    )

