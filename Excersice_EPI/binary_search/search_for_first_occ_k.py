def serach_first_k(A: [int], k: int) -> int:
    left, right, result = 0, len(A)-1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
k = 285

print(serach_first_k(A, k))
