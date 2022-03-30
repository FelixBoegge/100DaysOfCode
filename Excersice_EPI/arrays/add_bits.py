def add_bits(Bs, Bt):
    for i in reversed(range(len(Bs))):
        Bs[i] += Bt[i]
        if Bs[i] > 1:
            Bs[i] -= 2
            if i > 0:
                Bs[i - 1] += 1
            else:
                Bs.insert(0, 1)
    return Bs

Bs = [0,1,1,1,1,1,0]
Bt = [0,1,1,1,0,0,1]
print(Bs)
print(Bt)
print(add_bits(Bs, Bt))
