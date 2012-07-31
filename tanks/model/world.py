from .event import Event


class World(object):

    def __init__(self):
        self.items = set()
        self.item_added = Event()
        self.item_removed = Event()

    def __iter__(self):
        return iter(self.items)

    def add(self, item, **kwargs):
        for name, value in kwargs.iteritems():
            setattr(item, name, value)
        self.items.add(item)
        self.item_added(item)

    def remove(self, item):
        self.items.remove(item)
        self.item_removed(item)

