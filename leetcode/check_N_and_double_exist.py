def checkIfExist(arr: [int]) -> bool:
    h = {}
    for x in arr:
        if x in h.keys() or x in h.values():
            return True
        else:
            h[x * 2] = x / 2 if x % 2 == 0 else 0
    return False

arr = [3, 1, 7, 11]
print(checkIfExist(arr))
