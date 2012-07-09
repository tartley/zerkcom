from ..model import rect
from ..model.item import Item


def create():
    return Item(
        shape=rect.create(200, 200, 300, 210)
    )

