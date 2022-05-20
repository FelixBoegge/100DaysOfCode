def numDifferentIntegers(word: str) -> int:
    w = ''.join([c if c.isdigit() else ' ' for c in word]).split(' ')
    w = list(filter(lambda x: len(x) > 0, w))
    digits = []
    for digit in w:
        digit = str(int(digit))
        if digit not in digits:
            digits.append(digit)

    return len(digits)


word = "0a0123bc0134d8ef134"
print(numDifferentIntegers(word))
