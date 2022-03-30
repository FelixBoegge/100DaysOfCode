class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:

    def __init__(self):
        self.head = None

    # adds an element in front
    def prepend(self, data):
        node = Node(data, self.head)
        self.head = node

    # adds an element at the end
    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # adds elements at the end
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    # prints the Linkedlist
    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    # calculate the length of the Linkedlist
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # insert element with value at index
    def insert(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")
        if index == 0:
            self.prepend(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # deletes element at specific index
    def delete(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # removes element with spedific value
    def remove(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    # adds element with value after element with specific value
    def insert_behind_val(self, after, data):
        if self.head == None:
            return
        itr = self.head
        while itr:
            if itr.data == after:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next


if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values(['apple', 'mango', 'banana', 'passionfruit'])
    print("length: ", ll.get_length())
    ll.insert(2, 'grapes')
    ll.print()
    ll.remove('banana')
    ll.print()
    ll.append('papaya')
    ll.print()
    ll.insert_behind_val('passionfruit', 'cherry')
    ll.print()
    print(ll.get_length())

