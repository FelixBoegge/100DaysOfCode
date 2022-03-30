def increment(A):
    A[-1] += 1
    for i in range(len(A)-1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)

A = [9,9,9]
print(A)
increment(A)
print(A)
