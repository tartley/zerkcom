from OpenGL import GL
from OpenGL.GL.shaders import compileShader, compileProgram


_VERTEX = """
#version 120

attribute vec3 position;
attribute vec4 color;

varying vec4 baseColor;

void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * vec4(position, 1.0);
    baseColor = color;
}
"""

_FRAGMENT = """
#version 120

varying vec4 baseColor;

void main()
{
    gl_FragColor = baseColor;
}
"""


class Shader(object):
    '''
    Wraps PyOpenGL's shader compile and link functions

    .. function:: __init__(vertex, fragment, attributes)

        `vertex`: filename of vertex shader source code

        `fragment`: filename of fragment shader source code

        `attribs`: a list of attribute names

        Compiles and links the shader. For each attribute_name in
        `attribs`, looks up the attribute location, and stores it
        in self.attrib[attribute_name].
    '''
    def __init__(self):
        self.program = compileProgram(
            compileShader(_VERTEX, GL.GL_VERTEX_SHADER),
            compileShader(_FRAGMENT, GL.GL_FRAGMENT_SHADER)
        )
        self.attrib = {}
        for attrib in ['position', 'color']:
            self.attrib[attrib] = GL.glGetAttribLocation(self.program, attrib)


    def use(self):
        """Use this shader program"""
        GL.glUseProgram( self.program )


    @staticmethod
    def unuse():
        """Stop use of this shader program"""
        GL.glUseProgram( 0 )

