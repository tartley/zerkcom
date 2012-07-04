from pyglet import gl


CLEAR_COLOR_DEFAULT = (0.1, 0.2, 0.3, 1.0)


def clear_screen(color=CLEAR_COLOR_DEFAULT):
    '''
    Clear window color and depth buffers, using the given color
    '''
    r, g, b, _ = color
    gl.glClearColor(r, g, b, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

