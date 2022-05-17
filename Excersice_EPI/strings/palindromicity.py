def is_palindrome(s: str) -> bool:
    i, j = 0, len(s)-1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# pythonic approach
def is_pal(s: str) -> bool:
    return all(
        a == b
        for a, b in zip(map(str.lower, filter(str.isalnum, s)),
                        map(str.lower, filter(str.isalnum, reversed(s))))
    )

a = "Ray a Ray"
b = "A man, a plan, a canal, Panama!"
c = "Able was I, ere I saw Elba"
print(is_palindrome(a))
print(is_palindrome(b))
print(is_palindrome(c))
print(is_pal(a))
print(is_pal(b))
print(is_pal(c))

