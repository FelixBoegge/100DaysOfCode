def getRow(rowIndex: int):
    if not rowIndex:
        return [1]
    for i in range(1, rowIndex+1):
        new_current = [1]
        for j in range(1, i):
            new_current.append(current[j - 1] + current[j])
        new_current.append(1)
        current = new_current
    return current


print(getRow(10))