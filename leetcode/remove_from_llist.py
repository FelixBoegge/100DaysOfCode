from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

ll = Linked_list()
ll.append(Node(7))
ll.append(Node(7))
ll.append(Node(7))
ll.append(Node(7))
ll.print_ll()

def removeElements(head, val):
    root = prev = Node(0, head)
    cur = head
    while cur:
        if cur.data == val:
            prev.next = cur = cur.next
        else:
            prev, cur = cur, cur.next
    return root.next


val = 7
removeElements(ll.head, val)
