def parity(x):
    par = 0
    while x:
        par ^= 1
        x &= (x-1)
    return par


def parity_a(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


a = 11
b = 136
c = 7
print(parity(a))
print(parity(b))
print(parity(c))
