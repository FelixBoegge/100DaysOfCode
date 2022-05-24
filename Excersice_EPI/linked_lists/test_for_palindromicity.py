from linked_list import Node
from linked_list import Linked_list


L = Linked_list()

L.append(Node(1))
L.append(Node(2))
L.append(Node(3))
L.append(Node(4))
L.append(Node(4))
L.append(Node(3))
L.append(Node(2))
L.append(Node(1))

L.print_ll()

def palindromicity(L):
    def reverse_ll(L):
        prev = None
        curr = L
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    slow = fast = L
    length = 0
    while fast and fast.next:
        length += 2
        slow, fast = slow.next, fast.next.next

    first_half_iter, second_half_iter = L, reverse_ll(slow)
    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next
    return True


print(palindromicity(L.head))
