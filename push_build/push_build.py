"""
Node is defined in preloaded like this:
"""
class Node:
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    """push"""
    # Your code goes here.
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """build_one_two_three"""
    # Your code goes here.
    head = 1
    head = push(head, 2)
    head = push(head, 3)
    print(head)
