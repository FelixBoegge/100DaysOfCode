# training string
# s = 'The Tiger eats the Goat'
#
# print(s)
# print(s.split(' ')[1].split('g'))
# print(s.casefold())
# print(s.center(50, '-'))
# print(s.count('Goat', 0, 23))
# print(s.encode(encoding='ascii', errors='replace'))

# List slicing
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst[::])          # entire list
print(lst)              # entire list
print(lst[-9::1])       # entire list
print(lst[1:5])         # start slice left of index 1 and ends left of index 5
print(lst[-5:-9:-1])    # start slice right of index -3 and end right of index -7 going backwards (stepsize=-1)
print(lst[::3])         # entire list but only every third element
print(lst[1:5:2])       # 1-5 every second element
print(lst[:3:-1])       # start slicing on the right side (neg. stepsize), up to right of index 3
print(lst[-1:])         # last element
print(lst[:-1])         # all but not last element
print(lst[1:])          # all but not the first
print(lst[:1])          # first element
print(lst[::-1])        # all but reversed
print(" ")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listb = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

print(lista)
print(listb)
print(len(lista))
print(len(listb))

lista[2:4] = listb
print(lista)
print(len(lista))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
new_l = l[0:3]+l[7:]
print(new_l)
l = l[::2]+l[1::2]
print(l)

L1 = [1, 2, 3, 4, 5]
L2 = L1[:]
print(L1)
print(L2)
L1[3:3]= [6, 7, 8]
print(L1)
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L2[-2::-2])

g = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(g[-3:-6:-1])
print(g[-3:])
print(g[:-6])
print(g[-1:-3:-1])
print("Test:")
print(g[:3:-1])
print(g[-9::1])
print(g[-2::-2])
