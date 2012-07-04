
class Event(object):

    def __init__(self):
        self.listeners = set()

    def __iadd__(self, listener):
        self.listeners.add(listener)

    def __call__(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)


