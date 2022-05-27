from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


ll = Linked_list()

ll.append(Node(10))
ll.append(Node(4))
ll.append(Node(8))
ll.append(Node(3))

l = ll.head


def pairSum(head) -> int:
    def reverse(head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    max_pair = 0
    length = 0
    fast = slow = Node(0, head)
    while fast.next:
        length += 2
        fast, slow = fast.next.next, slow.next

    iter1 = head
    iter2 = reverse(slow.next)

    for _ in range(length // 2):
        pair = iter1.data + iter2.data
        if pair > max_pair:
            max_pair = pair
        iter1, iter2 = iter1.next, iter2.next

    return max_pair

print(pairSum(l))
