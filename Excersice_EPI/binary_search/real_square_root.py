import math


def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_square = mid * mid
        if mid_square > x:
            right = mid
        else:
            left = mid
    return left


x = 52
print(square_root(x))
