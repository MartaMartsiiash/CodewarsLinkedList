"""Loop"""

class Node:
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def loop_size(node):
    """loop_size"""
    slow = node
    fast = node

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count
