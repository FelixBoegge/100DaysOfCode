def generate(numRows: int):
    if not numRows:
        return []
    rows = [[1]]
    for i in range(1, numRows):
        current = []
        for j in range(i + 1):
            if j == 0 or j == i:
                next = 1
            else:
                next = rows[-1][j - 1] + rows[-1][j]
            current.append(next)
        rows.append(current)
    return rows

n = 30
print(generate(n))
