
class Item(object):
    '''
    A dumb colleciton of attributes, representing a single game world item.
    '''
    def __init__(self, **kwargs):
        print kwargs
        self.__dict__.update(kwargs)

