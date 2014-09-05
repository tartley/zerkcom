'''
Wrappers for PyOpenGL functions that are fiddly to use.
'''

import platform

from OpenGL import GL

__all__ = [
    'glGenVertexArray',
    'glBindVertexArray',
]


if platform.system() == 'Darwin':
    def glGenVertexArray_apple():
        vao_id = GL.GLuint(0)
        vertex_array_object.glGenVertexArraysAPPLE(1, vao_id)
        return vao_id.value
    glGenVertexArray = glGenVertexArray_apple
else:
    def glGenVertexArray_wrap():
        return GL.ARB.vertex_array_object.glGenVertexArrays(1)
    glGenVertexArray = glGenVertexArray_wrap


if platform.system() == 'Darwin':
    from OpenGL.GL.APPLE import vertex_array_object
    glBindVertexArray = vertex_array_object.glBindVertexArrayAPPLE
else:
    glBindVertexArray = GL.ARB.vertex_array_object.glBindVertexArray

