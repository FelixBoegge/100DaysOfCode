from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


ll = Linked_list()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.print_ll()
ll.connect(ll,2)

def hasCycle(head) -> bool:
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False

print(hasCycle(ll.head))
