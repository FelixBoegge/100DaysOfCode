class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [0] * capacity
        self._head = self._tail = self._length = 0

    def enqueue(self, x):
        if self._length == len(self._entries):
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head, self._tail = 0, self._length
            self._entries += [0] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._length += 1
        print(self._entries)

    def dequeue(self):
        self._length -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        print(self._entries)
        return result

    def size(self):
        return self._length

q = Queue(5)
print(q._entries)
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
print(q.dequeue())
q.enqueue(12)
print(q.dequeue())
print(q._entries)
print(q.dequeue())
q.enqueue(14)
q.enqueue(16)
q.enqueue(18)
