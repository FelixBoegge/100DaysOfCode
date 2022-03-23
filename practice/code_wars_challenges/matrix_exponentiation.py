def calc(matrix, n):
    dim = len(matrix[0])
    matnew = matrix
    for _ in range(1,n):
        mat = [[0 for i in range(dim)] for i in range(dim)]
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    mat[i][j] += matnew[i][k] * matrix[k][j]
        matnew = mat
    return mat

matrix = [[1, 2], [1, 0]]
n = 3
matrix2 = [[1, 2], [0, 1]]

print(calc(matrix2, n))
