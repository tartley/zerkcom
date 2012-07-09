
class Rect(object):

    def __init__(self, left, bottom, right, top):
        self.left = min(left, right)
        self.right = max(left, right)
        self.bottom = min(bottom, top)
        self.top = max(bottom, top)

