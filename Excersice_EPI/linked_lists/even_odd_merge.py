from linked_list import Node
from linked_list import Linked_list


L = Linked_list()

L.append(Node(0))
L.append(Node(1))
L.append(Node(2))
L.append(Node(3))
L.append(Node(4))
L.append(Node(5))
L.append(Node(6))

def even_odd_merge(L):
    if L == None:
        return L

    even_dummy_head, odd_dummy_head = Node(0), Node(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next

even_odd_merge(L.head).print_ll_from()
