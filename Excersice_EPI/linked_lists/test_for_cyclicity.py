from linked_list import Node
from linked_list import Linked_list


M = Linked_list()
M.append(Node(1))
M.append(Node(2))
M.append(Node(3))
M.append(Node(4))
M.append(Node(5))
M.append(Node(6))
M.make_cycle()

#M.print_ll()

def has_cylce(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it.data, cycle_len(slow)
    return None


print(f"cycle start: {has_cylce(M.head)[0]}", f"cycle length: {has_cylce(M.head)[1]}", sep="\n")
