from linked_list import Node
from linked_list import Linked_list


M = Linked_list()
M.append(Node(11))
M.append(Node(3))
M.append(Node(5))
M.append(Node(7))
M.append(Node(2))
M.print_ll()

def reverse_sublist(L, s, f):
    L = L.head
    dummy_head = sublist_head = Node(0, L)

    for _ in range(1, s):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(f - s):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next

reverse_sublist(M, 2, 4).print_ll_from()
