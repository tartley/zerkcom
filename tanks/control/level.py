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
        (-17, -5, -16, +5),
        (-18, -6, -16, -5),
        (-18, +5, -16, +6),
        # right home base
        (+16, -5, +17, +5),
        (+16, -6, +18, -5),
        (+16, +5, +18, +6),
        (-10, -1, -6, +1), # left island
        (+6, -1, +10, +1), # right island
        (-1, -10, +1, -6), # bottom island
        (-1, +6, +1, +10), # top island
    ]:
        world.add(wall.create(w * 16, s * 16, e * 16, n * 16))

    world.add(
        player.create(),
    )

