import collections


class Stack:
    StackWithCacheMax = collections.namedtuple('StackWithCacheMax', ('value', 'max'))

    def __init__(self):
        self.stack : [Stack.StackWithCacheMax] = []

    def push(self, val):
        self.stack.append(self.StackWithCacheMax(val, val if self.empty() else max(val, self.max())))

    def pop(self):
        return self.stack.pop().value

    def peak(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def max(self):
        return self.stack[-1].max
