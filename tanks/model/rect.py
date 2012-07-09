
def create(left, bottom, right, top):
    left = min(left, right)
    right = max(left, right)
    bottom = min(bottom, top)
    top = max(bottom, top)
    return [
        (left, bottom),
        (left, top),
        (right, top),
        (right, bottom),
    ]

