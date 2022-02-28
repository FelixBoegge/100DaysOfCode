# first method to create a 1d array
N = 5
arr = [0]*N
print(arr)

# second method to create a 1d array
M = 6
arr2 = [0 for i in range(M)]
print(arr2)

# using method1 to create a 2d array
rows, cols = 3, 4
arr1 = [[0]*cols]*rows
print(arr1)

# using method2 to create a 2d array
rows2, cols2 = 5, 6
arr2 = [[0 for i in range(cols2)] for j in range(rows2)]
print(arr2)

arr1[0][0] = 1
for row in arr1:
    print(row)

arr2[0][0] = 1
for row in arr2:
    print(row)

# creating a square matrix
print("#####".center(100, '-'))
x = 5
matrix = [[0 for _ in range(x)] for _ in range(x)]
for _ in range(x):
    matrix[_][_] = 1
for row in matrix:
    print(row)


# Tutorial
def prit(mat):
    print("")
    for r in mat:
        for c in r:
            print(str(c).rjust(2), end=" ")
        print("")


print("#####".center(100, '-'))
# Initialize and print
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

print(T[0])
print(T[1][2])
prit(T)

# insert at position 2 and print
T.insert(2, [0, 5, 11, 13, 6])
prit(T)

# reassign with indices
T[2] = [11, 9]
T[0][3] = 7
prit(T)

# deleting elements
del T[4]
prit(T)

# initialize new temperature chart with 3 measurements on 7 days.
print("#####".center(100, '-'))
m = 3
Tem = [[11, 21, 16], [13, 25, 17], [9, 18, 12], [10, 19, 17], [11, 23, 20], [14, 27, 22], [14, 28, 21]]
prit(Tem)
# avarage for every given time on day
avg = [0 for _ in range(m)]
for day in Tem:
    i = 0
    for daytime in day:
        avg[i] += daytime
        i += 1
avg = [avg[_]//len(Tem) for _ in range(m)]
Tem.append(avg)
prit(Tem)


