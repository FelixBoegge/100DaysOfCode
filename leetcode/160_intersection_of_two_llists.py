from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

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


def getIntersectionNode(headA, headB):
    def length(l):
        length = 0
        while l:
            length += 1
            l = l.next
        return length

    if length(headA) > length(headB):
        headA, headB = headB, headA
    for _ in range(abs(length(headA) - length(headB))):
        headB = headB.next

    while headA and headB and headA is not headB:
        headA, headB = headA.next, headB.next

    return headA

print(getIntersectionNode(L1.head, L2.head).data)
