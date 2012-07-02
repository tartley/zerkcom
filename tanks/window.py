import pyglet

def create_window(options):
    return pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=True,
        resizable=True,
        caption='Adventure',
    )

