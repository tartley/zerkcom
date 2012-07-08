

def init(window, world):

    def on_item_added(item):
        if hasattr(item, 'keys'):
            window.push_handlers(item.keys)

    def on_item_removed(item):
        if hasattr(item, 'keys'):
            window.remove_handlers(item.keys)

    world.item_added += on_item_added
    world.item_removed += on_item_removed

