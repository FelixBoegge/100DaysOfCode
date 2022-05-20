def backspaceCompare(s: str, t: str) -> bool:
    stemp = ""
    ttemp = ""
    for c in s:
        if c != '#':
            stemp += c
        if c == '#' and stemp:
            stemp = stemp[:-1]

    for c in t:
        if c != '#':
            ttemp += c
        if c == '#' and ttemp:
            ttemp = ttemp[:-1]

    return stemp == ttemp

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))