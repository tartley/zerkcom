import os

import pyglet
from pkg_resources import resource_listdir, resource_stream


def _get_name(filename):
    return os.path.splitext(os.path.basename(filename))[0]


def _load_image(filename):
    texture = pyglet.image.load(
        filename,
        resource_stream('zerkcom', filename)
    ).get_texture()
    texture.anchor_x = texture.width / 2.0
    texture.anchor_y = texture.height / 2.0
    return texture


def load_all(directory):
    return {
        _get_name(filename): _load_image(directory + '/' + filename)
        for filename in resource_listdir('zerkcom', directory)
    }

