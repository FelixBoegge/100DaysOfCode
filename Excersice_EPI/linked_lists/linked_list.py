class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def print_ll_from(self):
        current = self
        while current is not None:
            print(current.data, "--> ", end='')
            current = current.next
        print("None")


class Linked_list:
    def __init__(self, head=None):
        self.head = head


    def search_node(self, L, key):
        while L and L.data != key:
            L = L.next
        return L


    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node


    def append(self, node):
        if self.head == None:
            self.head = node
            return
        current = self.head
        while True:
            if current.next == None:
                current.next = node
                break
            current = current.next


    def delete_after(self, node):
        node.next = node.next.next


    def print_ll(self):
        current = self.head
        while current is not None:
            print(current.data, "--> ", end='')
            current = current.next
        print("None")
