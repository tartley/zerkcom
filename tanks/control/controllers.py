import pyglet

from . import keyhandlers

def init(win, world):
    keyhandlers.init(win, world)

    def update(dt):
        for item in world:
            if hasattr(item, 'update'):
                item.update(item, dt)
        win.invalid = True

    pyglet.clock.schedule(update)

