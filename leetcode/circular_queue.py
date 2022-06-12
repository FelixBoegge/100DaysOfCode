class CircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.head = self.tail = self.length = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.length += 1
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % len(self.q)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.length -= 1
            self.q[self.head] = 0
            self.head = (self.head + 1) % len(self.q)
            return True
        return False

    def Front(self) -> int:
        return self.q[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.q[self.tail - 1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == len(self.q)

    def length(self) -> int:
        return self.length
