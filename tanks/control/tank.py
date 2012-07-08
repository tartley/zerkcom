from math import sin, cos

from py2d.Math import Vector


TURN_RATE = 0.02
SPEED = 2.0

def update_tank(item, dt):
    item.angle += (item.speed_right - item.speed_left) * TURN_RATE
    item.position += Vector(-sin(item.angle), cos(item.angle)) * \
        (item.speed_left + item.speed_right) * SPEED

