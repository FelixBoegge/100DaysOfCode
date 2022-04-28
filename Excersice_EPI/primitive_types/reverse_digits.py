def reverse_digits(x: int) -> int:
    res, x_remain = 0, abs(x)
    while x_remain:
        res = res * 10 + x_remain % 10
        x_remain //= 10
    return -res if x < 0 else res


x = -1234
print(reverse_digits(x))
