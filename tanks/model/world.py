
from .event import Event


class World(object):

    def __init__(self):
        self.items = set()
        self.item_added = Event()
        self.item_removed = Event()

    def add(self, item, position=None):
        self.items.add(item)
        self.item_added(item)

    def remove(self, item):
        self.items.remove(item)
        self.item_removed(item)

