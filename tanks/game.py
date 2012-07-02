

class Item():
    def __init__(self):
        self.position = 1.0, 2.0
        self.size = 2.0, 3.0


def start(world):
    world.clear()
    world.add(Item())

