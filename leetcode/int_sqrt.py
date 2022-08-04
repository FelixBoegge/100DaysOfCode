def mySqrt(x: int) -> int:
    left, right = 0, x
    while left <= right:
        pivot = (left + right) // 2
        pivot_sq = pivot * pivot
        if pivot_sq == x:
            return pivot
        elif pivot_sq < x:
            left = pivot + 1
        else:
            right = pivot - 1
    return left-1

x = 8
print(x)
print(mySqrt(x))
