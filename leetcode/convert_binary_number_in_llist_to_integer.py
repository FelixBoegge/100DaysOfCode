from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list

ll = Linked_list()
ll.append(Node(1))
ll.append(Node(0))
ll.append(Node(1))
ll.append(Node(1))
ll.print_ll()

def getDecimalValue(head) -> int:
    num = 0
    count = 0

    def reverseList(head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    cur = reverseList(head)
    while cur:
        num += cur.data * 2 ** count
        count += 1
        cur = cur.next

    return num

print(getDecimalValue(ll.head))
