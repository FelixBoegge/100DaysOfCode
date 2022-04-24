def sprial_ordering(matrix):
    shift = ((0, 1), (1, 0), (0,-1), (-1, 0))
    direction = x = y = 0
    spiral = []

    for _ in range(len(matrix)**2):
        spiral.append(matrix[x][y])
        matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if (next_x not in range(len(matrix)) or next_y not in range(len(matrix)) or matrix[next_x][next_y] == 0):
            direction = (direction+1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral

A = []
B = [[1]]
C = [[1,2], [3,4]]
D = [[1,2,3], [4,5,6], [7,8,9]]
E = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

print(sprial_ordering(A))
print(sprial_ordering(B))
print(sprial_ordering(C))
print(sprial_ordering(D))
print(sprial_ordering(E))
