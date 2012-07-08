

def init(window, world):

    def on_item_added(item):
        if hasattr(item, 'keyhandler'):
            window.push_handlers(item.keyhandler)

    def on_item_removed(item):
        if hasattr(item, 'keyhandler'):
            window.remove_handlers(item.keyhandler)

    world.item_added += on_item_added
    world.item_removed += on_item_removed

