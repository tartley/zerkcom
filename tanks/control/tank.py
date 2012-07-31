from collections import namedtuple
from math import sin, cos

from py2d.Math import Vector


TURN_RATE = 0.02
SPEED = 2.0


Inputs = namedtuple('Inputs', ['left_tread', 'right_tread'])


def update(item, controls, dt):
    item.angle += (controls.left_tread - controls.right_tread) * TURN_RATE
    item.position += Vector(cos(item.angle), sin(item.angle)) * \
        (controls.left_tread + controls.right_tread) * SPEED

