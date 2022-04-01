def delete_duplicates(a):
    if not a:
        return 0

    write_index = 1
    for i in range(1, len(a)):
        if a[write_index-1] != a[i]:
            a[write_index] = a[i]
            write_index += 1
    return write_index


def delete_duplicates2(a, key):
    if not a:
        return 0

    write_index = 1
    for i in range(1, len(a)):
        if a[write_index-1] != key:
            a[write_index] = a[i]
            write_index += 1
    return write_index


a = [2,3,5,5,7,11,11,11,13]
print(len(a))
key = 2
print(delete_duplicates(a))
print(delete_duplicates2(a, key))

