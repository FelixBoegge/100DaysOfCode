def maxDepth(s: str) -> int:
    cur = 0
    depth = 0
    for c in s:
        if c == "(":
            cur += 1
            if cur > depth:
                depth = cur
        elif c == ")":
            cur -= 1
    return depth

