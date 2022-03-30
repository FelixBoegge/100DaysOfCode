def sort(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

A = [45, 13, 10, 4, 5, 0, 34, 28, 40]
pivot_index = 1

print(A)
sort(pivot_index, A)
print(A)
