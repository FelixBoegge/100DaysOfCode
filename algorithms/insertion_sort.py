def insertion_sort(a):
    size = len(a)
    for i in range(1, size):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp


test = [78, 34, 6, 632, -1, 32, 75, 45, 4, 5, 0, 1111, 1232, 43, 343, 3, 43]
print(test)
insertion_sort(test)
print(test)
