from linked_list import Node
from linked_list import Linked_list


L1 = Linked_list()
L2 = Linked_list()

L1.append(Node(2))
L1.append(Node(5))
L1.append(Node(7))
L2.append(Node(3))
L2.append(Node(11))

L1.print_ll()
L2.print_ll()

def merge_two_sorted_llists(L1, L2):
    dummy_head = tail = Node()
    L1, L2 = L1.head, L2.head

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


merge_two_sorted_llists(L1, L2).print_ll_from()
