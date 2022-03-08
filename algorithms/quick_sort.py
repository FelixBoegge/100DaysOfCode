def partition(a, start, end):
    pivot_index = start
    pivot = a[pivot_index]
    while start < end:
        while start < len(a) and a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, a)
    swap(pivot_index, end, a)
    return end


def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def quick_sort(a, start, end):
    if start < end:
        pi = partition(a, start, end)
        quick_sort(a, start, pi-1)      # left partition
        quick_sort(a, pi+1, end)        # right partition


test = [78, 34, 6, 632, -1, 32, 75, 45, 4, 5, 0, 1111, 1232, 43, 343, 3, 43]
print(test)
quick_sort(test, 0, len(test)-1)
print(test)
