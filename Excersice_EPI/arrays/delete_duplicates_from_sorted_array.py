def delete_duplicates(a):
    temp = a[0]
    for i in range(1,len(a)):
        if a[i] == temp:
            del a[i]
            a.append(0)
        else:
            temp = a[i+1]
    return a


a = [2,2,3,3,5,5,7,11,11,11,13]
print(delete_duplicates(a))
