from linked_list import Node
from linked_list import Linked_list


L1 = Linked_list()

L1.append(Node(1))
L1.append(Node(2))
L1.append(Node(3))
L1.append(Node(4))
L1.append(Node(5))
L1.append(Node(6))

def remove_kth_last_element(l, k):
    dummy_head = Node(0, l)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy_head.next

L1.print_ll()
remove_kth_last_element(L1.head, 4)
L1.print_ll()
