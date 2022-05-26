from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


ll = Linked_list()

ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))

l= ll.head

def swapPairs(head):
    dummy_head = prev = Node(0, head)
    cur = head
    if not head or not head.next:
        return head

    while cur and cur.next:
        temp = cur.next
        if cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        prev.next = temp
        temp.next = cur
        prev = cur
        cur = cur.next

    return dummy_head.next

swapPairs(l)

