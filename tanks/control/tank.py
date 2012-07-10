from math import sin, cos

from py2d.Math import Vector


TURN_RATE = 0.02
SPEED = 2.0

def update_tank(item, dt):
    item.angle += (item.speed_left - item.speed_right) * TURN_RATE
    item.position += Vector(cos(item.angle), sin(item.angle)) * \
        (item.speed_left + item.speed_right) * SPEED

