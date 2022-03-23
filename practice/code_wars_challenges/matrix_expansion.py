def expansion(matrix, n):
    for _ in range(n):
        dim = len(matrix[0])
        new_line = [0 for i in range(dim)]
        corner = 0
        for i in range(dim):
            matrix[i].append(sum(matrix[i]))
            for j in range(dim):
                new_line[j] += matrix[i][j]
                if i==j:
                    corner += matrix[i][j]
        new_line.append(corner)
        matrix.append(new_line)
    return matrix

matrix = [[4, 1], [19, -2]]
n = 2
print(expansion(matrix, n))

