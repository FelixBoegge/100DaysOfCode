def shell_sort(a):
    size = len(a)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            p = a[i]
            j = i
            while j >= gap and a[j-gap] > p:
                a[j] = a[j-gap]
                j -= gap
            a[j] = p
        gap = gap // 2


test = [21, 38, 29, 17, 5, 25, 11, 32, 9]
#test = [78, 34, 6, 632, -1, 32, 75, 45, 4, 5, 0, 1111, 1232, 43, 343, 3, 43]
print(test)
shell_sort(test)
print(test)
