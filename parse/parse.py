"""Parse"""
class Node:
    """Node"""
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """linked_list_from_string"""
    if list_repr == "null":
        return None
    res = None
    l = list_repr.strip().split(" -> ")
    for dat in l[::-1]:
        if dat == "null":
            continue
        res = Node(dat, res)
    return res

# if __name__ == '__main__':
#     l = linked_list_from_string("1 -> 2 -> 3 -> null")
#     while l:
#         print(l.data)
#         l = l.next
