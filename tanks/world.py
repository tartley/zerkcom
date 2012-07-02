
class World():

    def __init__(self):
        self.items = set()

    def add(self, item, position=None):
        self.items.add(item)

    def remove(self, item):
        self.items.remove(item)

