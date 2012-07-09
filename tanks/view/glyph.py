
def get_glyph(verts):
    pass # TODO


def init(window, world):

    def on_item_added(item):
        if hasattr(item, 'verts'):
            item.glyph = get_glyph(item.verts)

    def draw_glyphs():
        for item in world:
            if hasattr(item, 'glyph'):
                pass # TODO

    return draw_glyphs

