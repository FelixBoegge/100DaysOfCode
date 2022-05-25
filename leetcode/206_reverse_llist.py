from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

ll = Linked_list()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.print_ll()

def reverseList(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

reverseList(ll.head)
ll.print_ll()
