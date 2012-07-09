
class Rect(object):

    def __init__(self, left, bottom, right, top):
        left = min(left, right)
        right = max(left, right)
        bottom = min(bottom, top)
        top = max(bottom, top)
        self.verts = [
            (left, bottom),
            (left, top),
            (right, top),
            (right, bottom),
        ]

