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

