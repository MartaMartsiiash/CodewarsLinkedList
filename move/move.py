"""Move"""
class Node(object):
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """Context"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Move node"""
    # Your code goes here.
    # Remember to return the context.
    if source:
        removed_node = source
        source = source.next
        removed_node.next = dest
        dest = removed_node
        return Context(source, dest)
    raise ValueError
