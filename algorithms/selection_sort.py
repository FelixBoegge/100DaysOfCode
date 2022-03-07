def selection_sort(a):
    size = len(a)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]


test = [78, 34, 6, 632, -1, 32, 75, 45, 4, 5, 0, 1111, 1232, 43, 343, 3, 43]
print(test)
selection_sort(test)
print(test)
