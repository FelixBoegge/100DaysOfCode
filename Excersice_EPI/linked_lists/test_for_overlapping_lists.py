from linked_list import Node
from linked_list import Linked_list


L1 = Linked_list()
L2 = Linked_list()

L1.append(Node(1))
L1.append(Node(2))
L1.append(Node(3))
L1.append(Node(4))
L1.append(Node(5))
L1.append(Node(6))

L2.append(Node(9))
L2.append(Node(8))
L2.append(Node(7))


L2.connect(L1, 2)

L1.print_ll()
L2.print_ll()

def overlapping(l1, l2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    if length(l1) > length(l2):
        l1, l2 = l2, l1
    for _ in range(abs(length(l1)-length(l2))):
        l2 = l2.next

    while l1 and l2 and l1 is not l2:
        l1, l2 = l1.next, l2.next
    return l1.data


print(overlapping(L1.head, L2.head))
