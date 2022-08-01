def search_smallest(A: [int]) -> int:
    left, right = 0, len(A)-1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left


A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
B = [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
print(search_smallest(A))
