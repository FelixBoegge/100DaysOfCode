def pow(x: float, y: int) -> float:
    res, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0/x
    while power:
        if power & 1:
            res *= x
        x, power = x*x, power >> 1
    return res


a = 0.5
b = -2
# a=3 and b=4 should return 91
print(pow(a, b))
