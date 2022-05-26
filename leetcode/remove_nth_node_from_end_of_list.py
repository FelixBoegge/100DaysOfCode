from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


ll1 = Linked_list()

ll1.append(Node(1))
ll1.append(Node(4))
ll1.append(Node(8))
ll1.append(Node(3))

l= ll1.head
n = 3

def removeNthFromEnd(head, n):
    dummy_head = iter1 = iter2 = Node(0, head)
    for _ in range(n):
        iter1 = iter1.next

    while iter1.next:
        iter1, iter2 = iter1.next, iter2.next

    iter2.next = iter2.next.next

    return dummy_head.next

ll1.print_ll()
removeNthFromEnd(l, n)
ll1.print_ll()
