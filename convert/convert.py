"""Convert"""
class Node():
    """Node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    """stringify"""
    res = ""
    probe = node
    while probe:
        res += f"{probe.data} -> "
        probe = probe.next
    res += "None"
    return res
