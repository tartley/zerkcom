import ctypes 
import itertools

from OpenGL import GL
from OpenGL.arrays import vbo

from .shader import Shader
from . import glwrap


type_to_enum = {
    GL.GLubyte: GL.GL_UNSIGNED_BYTE,
    GL.GLushort: GL.GL_UNSIGNED_SHORT,
    GL.GLuint: GL.GL_UNSIGNED_INT,
}


def get_index_type(num_verts):
    '''
    Return the unsigned integer data type required to store the given number.
    e.g. 255 can be stored in a GLubyte, whereas 256 rrequires a GLushort.
    '''
    if num_verts < 256:
        return GL.GLubyte
    elif num_verts < 65536:
        return GL.GLushort
    else:
        return GL.GLuint


def array(type_, seq):
    '''
    Puts the given sequence into a ctypes array of the given ctype.
    [ 1, 2, 3, 4, 5, 6 ] -> (GLfloat*6)(1, 2, 3, 4, 5, 6)
    '''
    # construct then populate [:] is faster than constructing with *seq
    carray = (type_ * len(seq))()
    carray[:] = seq
    return carray


class Glyph(object):
     # TODO convert this to using an index array then rendering only needs bind
     # the VAO, so storing self.glindices, self.etc is not reqd and we can just
     # beome a function that returns vao id

     # TODO floats per vertex, position, and color should be passed in,
     # provided by whatever produced the vertex data

    def __init__(self, verts, indices, shader):
        Glyph.shader = shader
        self.vbo = vbo.VBO(
            array(GL.GLfloat, verts),
            usage='GL_STATIC_DRAW',
        )
        FLOATS_PER_VERTEX = 6 # (x, y, r, g, b, a)
        index_type = get_index_type(len(verts) / FLOATS_PER_VERTEX)
        self.glindices = array(index_type, indices)
        self.index_type = type_to_enum[index_type]
        self.vao = glwrap.glGenVertexArray()
        glwrap.glBindVertexArray(self.vao)
        try:
            self.vbo.bind()

            GL.glEnableVertexAttribArray(shader.attrib['position'])
            GL.glEnableVertexAttribArray(shader.attrib['color'])

            STRIDE = FLOATS_PER_VERTEX * ctypes.sizeof(GL.GLfloat)
            FLOATS_PER_POSITION = 2
            FLOATS_PER_COLOR = 4
            offset = 0
            GL.glVertexAttribPointer(
                shader.attrib['position'], FLOATS_PER_POSITION, GL.GL_FLOAT,
                False, STRIDE, ctypes.c_void_p(offset)
            )
            offset += FLOATS_PER_POSITION * ctypes.sizeof(GL.GLfloat)
            GL.glVertexAttribPointer(
                shader.attrib['color'], FLOATS_PER_COLOR, GL.GL_FLOAT,
                False, STRIDE, ctypes.c_void_p(offset)
            )
        finally:
            glwrap.glBindVertexArray(0)


def _tessellate(indices):
    '''
    Return the indices of the given face tesselated into triangles The
    triangles will be wound in the same direction as the original poly. Does
    not work for concave faces.

    e.g. [0, 1, 2, 3, 4] -> [0, 1, 2,  0, 2, 3,  0, 3, 4]
    '''
    for index in xrange(1, len(indices) - 1):
        yield indices[0]
        yield indices[index]
        yield indices[index + 1]
    

def get_verts_or_indices(polys, indices=False):
    result = []
    next_index = 0
    new_indices = {} # vertex : new_index
    for color, positions in polys:
        for position in _tessellate(positions):
            vertex = tuple(itertools.chain(position, color))

            if vertex not in new_indices:
                new_indices[vertex] = next_index
                next_index += 1
                result.append(new_indices[vertex] if indices else vertex)
            elif indices:
                result.append(new_indices[vertex])

    return result


def get_vertices(polys):
    return get_verts_or_indices(polys)

def get_indices(polys):
    return get_verts_or_indices(polys, indices=True)

def get_glyph(positions, shader):
    '''
    input is
    [
        (color, [position, position, position...]),
        ...
    ]
    where:
        color = 4 tuple
        position = 2 tuple
    output is:
        (
            GL.GLfloat(V)(vertex, vertex, vertex...),
            GL.GLubyte(I)(index, index, index...),
        )
    where:
        'V' is number of vertices * floats per vertex,
        A vertex consists of floats (x, y, r, g, b, a),
        'I' is number of indices,
        Type of index array might be ubyte, ushort, uint, depending on number
        of indices,
    '''
    polys = [((1, 0, 0, 1), positions)]
    return Glyph(
        list(itertools.chain.from_iterable(get_vertices(polys))),
        get_indices(polys),
        shader)


def init(window, world):

    shader = Shader()

    def on_item_added(item):
        if hasattr(item, 'shape'):
            item.glyph = get_glyph(item.shape, shader)

    world.item_added += on_item_added

    def draw_glyphs():
        shader = None
        for item in world:
            if hasattr(item, 'glyph'):

                GL.glPushMatrix()

                #if hasattr(item, 'position'):
                    #GL.glTranslatef(*item.position)

                #if orientation and orientation != Orientation.Identity:
                    #GL.glMultMatrixf(orientation.matrix)

                if item.glyph.shader is not shader:
                    shader = item.glyph.shader
                    shader.use()

                glwrap.glBindVertexArray(item.glyph.vao)

                GL.glDrawElements(
                    GL.GL_TRIANGLES,
                    len(item.glyph.glindices),
                    item.glyph.index_type,
                    item.glyph.glindices
                )

                GL.glPopMatrix()

        glwrap.glBindVertexArray(0)
        Shader.unuse()

    return draw_glyphs

