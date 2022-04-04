def generate(numRows: int):
    if not numRows:
        return []
    rows = [[1]]
    for i in range(1, numRows):
        current = [1]
        for j in range(1, i):
            current.append(rows[-1][j - 1] + rows[-1][j])
        current.append(1)
        rows.append(current)
    return rows

n = 30
print(generate(n))
