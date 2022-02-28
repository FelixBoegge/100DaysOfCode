import array

a = array.array('i', [1, 2, 3])
for i in range(len(a)):
    print(a[i], end=" ")
print("")

a.append(8)
a.append(3)
a.insert(2, 5)

for i in range(len(a)):
    print(a[i], end=" ")
print("")

k = a.pop(0)
print(f"{k} was popped from a")
a.remove(3)

for i in range(len(a)):
    print(a[i], end=" ")
print("")

k = a.index(8)
print(f"{k} is index of 8")
a.reverse()

for i in range(len(a)):
    print(a[i], end=" ")
print("")

