"""Get nth Node"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """get nth"""
    probe = node
    count = 0
    while probe:
        count += 1
        probe = probe.next
    if index in range(0, count):
        for _ in range(index):
            node = node.next
        return node
    raise ValueError

# if __name__ == '__main__':
#     n1 = Node(2, Node(4, Node(3)))
#     print(get_nth(n1, 2).data)
