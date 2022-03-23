def rotate_against_clockwise(matrix, times):
    rots = times%4
    dim = len(matrix[0])
    for _ in range(rots):
        mat = [[0 for i in range(dim)] for i in range(dim)]
        for j in range(dim):
            for k in range(dim):
                mat[j][k] = matrix[k][dim-j-1]
        matrix = mat
        print(matrix)
    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[1,2,3], [4,5,6], [7,8,9]]
times = 2

rotate_against_clockwise(matrix2, times)
