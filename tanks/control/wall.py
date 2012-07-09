from ..model.item import Item
from ..model.rect import Rect


def create():
    return Item(
        shape=Rect(200, 200, 300, 210)
    )

