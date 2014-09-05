
def create(left, bottom, right, top):
    left, right = sorted([left, right])
    bottom, top = sorted([bottom, top])
    return [
        (left, bottom),
        (left, top),
        (right, top),
        (right, bottom),
    ]

