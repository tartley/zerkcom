import pyglet
from pyglet import gl


CLEAR_COLOR_DEFAULT = (0.1, 0.2, 0.3, 1.0)


def create(options):
    return pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        resizable=not options.fullscreen,
        caption='Tanks',
    )


def clear(color=CLEAR_COLOR_DEFAULT):
    r, g, b, _ = color
    gl.glClearColor(r, g, b, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

