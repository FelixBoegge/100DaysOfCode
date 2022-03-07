def bubble_sort(a):
    size = len(a)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break


test = [78, 34, 6, 632, -1, 32, 75, 45, 4, 5, 0, 1111, 1232, 43, 343, 3, 43]
print(test)
bubble_sort(test)
print(test)
