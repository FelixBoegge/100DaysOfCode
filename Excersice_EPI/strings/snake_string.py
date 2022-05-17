def snake_string(s: str) -> str:
    result = []
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)

# more pythonic approach
def snake(s):
    return s[1::4] + s[::2] + s[3::4]

s = 'Hello World!'
print(snake_string(s))
print(snake(s))
