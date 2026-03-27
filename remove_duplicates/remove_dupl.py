"""Remove duplicates"""
class Node(object):
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """remove_duplicates"""
    # Your code goes here.
    # Remember to return the head of the list.
    if not head or not head.next:
        return head
    probe = head
    while probe and probe.next:
        if probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head
