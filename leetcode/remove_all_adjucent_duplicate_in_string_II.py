def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            if stack[-1][1] == k - 1:
                while stack and stack[-1][0] == c:
                    stack.pop()
            else:
                stack.append((c, stack[-1][1] + 1))
        else:
            stack.append((c, 1))

    return ''.join(x[0] for x in stack)


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k))
