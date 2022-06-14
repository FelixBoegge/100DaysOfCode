class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if len(self.stack) > 0 else -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > k:
            for i in range(k):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val
