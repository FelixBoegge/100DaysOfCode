from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

ll1 = Linked_list()
ll2 = Linked_list()

ll1.append(Node(1))
ll1.append(Node(4))
ll1.append(Node(8))
ll1.append(Node(3))

ll2.append(Node(5))
ll2.append(Node(9))
ll2.append(Node(6))
ll2.append(Node(6))

ll1.print_ll()
ll2.print_ll()

l1 = ll1.head
l2 = ll2.head


def addTwoNumbers(l1, l2):
    def reverseList(head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    l1, l2 = reverseList(l1), reverseList(l2)

    iter = dummy_head = Node()
    carry = 0
    while l1 or l2 or carry:
        val = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        iter.next = Node(val % 10)
        iter, carry = iter.next, val // 10

    return reverseList(dummy_head.next)

addTwoNumbers(l1, l2).print_ll_from()
