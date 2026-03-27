"""Split"""
class Node(object):
    """Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """Context"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """alternating_split"""
    if head is None or head.next is None:
        raise ValueError

    first_head = None
    second_head = None
    first_tail = None
    second_tail = None

    is_first = True

    while head:
        next_node = head.next
        head.next = None

        if is_first:
            if first_head is None:
                first_head = first_tail = head
            else:
                first_tail.next = head
                first_tail = head
        else:
            if second_head is None:
                second_head = second_tail = head
            else:
                second_tail.next = head
                second_tail = head

        is_first = not is_first
        head = next_node

    return Context(first_head, second_head)
