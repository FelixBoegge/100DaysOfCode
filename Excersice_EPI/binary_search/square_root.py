def square_root(k: int) -> int:
    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        mid_sqrt = mid * mid
        if mid_sqrt <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


k = 25
print(square_root(k))
