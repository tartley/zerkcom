from ..model import rect
from ..model.item import Item


def create(xmin, ymin, xmax, ymax):
    return Item(
        shape=rect.create(xmin, ymin, xmax, ymax),
    )

