class Solution:
    def asteroidCollision(self, asteroids:[int]):
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and (stack[-1] < 0 and stack[-2] > 0):
                a = stack.pop()
                b = stack.pop()
                if abs(a) == abs(b):
                    continue
                else:
                    if abs(a) > abs(b):
                        stack.append(a)
                    else:
                        stack.append(b)
        return stack