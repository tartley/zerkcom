from pkg_resources import resource_stream
import pyglet
from pyglet import gl


CLEAR_COLOR_DEFAULT = (0.1, 0.2, 0.3, 1.0)


def clear_screen(color=CLEAR_COLOR_DEFAULT):
    '''
    Clear window color and depth buffers, using the given color
    '''
    r, g, b, _ = color
    gl.glClearColor(r, g, b, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)



def get_sprite(name):
    image = pyglet.image.load(
        '%s.png' % (name,),
        resource_stream('tanks', 'data/%s.png' % (name,)),
    )
    sprite = pyglet.sprite.Sprite(image)
    sprite.scale = 4
    return sprite


def init(window, world):

    @window.event
    def on_draw():
       clear_screen()
       for item in world:
           item._sprite.draw()

    def on_item_added(item):
        item._sprite = get_sprite(item.sprite)

    def on_item_removed(item):
        pass

    world.item_added += on_item_added
    world.item_removed += on_item_removed

