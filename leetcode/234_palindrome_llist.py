from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


ll = Linked_list()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(2))
ll.append(Node(1))
ll.print_ll()

def isPalindrome(head) -> bool:
    def reverse_ll(head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    iter1, iter2 = head, reverse_ll(slow)
    while iter1 and iter2:
        if iter1.data != iter2.data:
            return False
        iter1, iter2 = iter1.next, iter2.next

    return True

print(isPalindrome(ll.head))
