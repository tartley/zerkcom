from ..model import rect
from ..model.item import Item


def create(xmin, ymin, xmax, ymax, color):
    return Item(
        shape=(color, rect.create(xmin, ymin, xmax, ymax)),
    )

