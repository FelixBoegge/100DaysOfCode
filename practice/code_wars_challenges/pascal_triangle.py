def generate_diagonal(n, l):
    res = []
    for x in range(1, l + 1):
        res.append(pascal(n, x))
    return res

d = {}

def pascal(n, p):
    if n == 0 or p == 1:
        return 1
    if str(n)+" "+str(p) in d.keys():
        return d[str(n)+" "+str(p)]
    else:
        d[str(n) + " " + str(p)] = (pascal(n, p - 1) + pascal(n - 1, p))
    return pascal(n, p - 1) + pascal(n - 1, p)

n = 87
l = 50
print(generate_diagonal(n, l))
