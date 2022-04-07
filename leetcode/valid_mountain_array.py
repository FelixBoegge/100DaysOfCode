def validMountainArray(arr) -> bool:
    if len(arr) < 3:
        return False
    i = 0
    peak = 0
    while arr[i + 1] > arr[i]:
        i += 1
        peak = 1
        if i == len(arr) - 1:
            return False
    while arr[i + 1] < arr[i]:
        i += 1
        if i == len(arr) - 1:
            if peak == 1:
                return True
            return False
    if i == len(arr) and peak == 1:
        return True
    return False

arr = [3,5]
print(validMountainArray(arr))
