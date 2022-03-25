def sum_pairs(a, s):
    d = {}
    for num in a:
        if s-num in d.keys():
            return [s-num, num]
        else:
            d[num] = 1
    return None

a= [10, 4, 15, 7, 3, 8]
s=18

print(sum_pairs(a, s))
