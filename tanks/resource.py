import os

import pyglet
from pkg_resources import resource_listdir, resource_stream


def load_image(filename):
    return pyglet.image.load(
        filename,
        resource_stream('tanks', filename)
    )


def load_images(directory):
    images = {}
    for filename in resource_listdir('tanks', directory):
        name, _ = os.path.splitext(os.path.basename(filename))
        images[name] = load_image(directory + '/' + filename)
    return images

