from colortuple import Color
from py2d.Math import Vector

from . import player
from . import wall


def start(world):

    for w, s, e, n in [
        # exterior walls
        (-24, +13, +24, +14), # top
        (-24, -14, +24, -13), # bottom
        (-24, -14, -23, +14), # left
        (+23, -14, +24, +14), # right
        # left home base
        (-17, -4, -16, +4),
        (-18, -5, -16, -4),
        (-18, +4, -16, +5),
        # right home base
        (+16, -4, +17, +4),
        (+16, -5, +18, -4),
        (+16, +4, +18, +5),
        # islands
        (-10, -1, -6, +1), # left
        (+6, -1, +10, +1), # right
        (-1, -10, +1, -6), # bottom
        (-1, +6, +1, +10), # top
    ]:
        world.add(
            wall.create(w * 16, s * 16, e * 16, n * 16, Color(0.1, 0.6, 0.3))
        )

    world.add(
        player.create(),
        position=Vector(-325, 0),
        angle=0.0,
    )

