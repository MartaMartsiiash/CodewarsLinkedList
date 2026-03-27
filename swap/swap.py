"""Swap"""
class Node:
    """Node"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """swap"""
    if not head or not head.next:
        return head

    new_head = head.next
    prev = None
    curr = head

    while curr and curr.next:
        first = curr
        second = curr.next
        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        curr = first.next

    return new_head
