import itertools


def look_and_say(n: int) -> str:
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                count += 1
                i += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

# pythonic approach
def look_say(n):
    s = '1'
    for _ in range(n-1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

n = 5
print(look_and_say(n))
print(look_say(n))
