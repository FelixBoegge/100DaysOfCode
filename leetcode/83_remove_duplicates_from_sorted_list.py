from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

ll = Linked_list()
ll.append(Node(1))
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(2))
ll.print_ll()

def deleteDuplicates(head):
    cur = head
    while cur:
        next_distinct = cur.next
        while next_distinct and next_distinct.data == cur.data:
            next_distinct = next_distinct.next
        cur.next = next_distinct
        cur = next_distinct
    return head

deleteDuplicates(ll.head)
ll.print_ll()
