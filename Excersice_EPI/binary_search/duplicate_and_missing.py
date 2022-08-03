import collections
import functools

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))

def duplicate_missing(A: [int]) -> DuplicateAndMissing:
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    differ_bit, miss_or_dub = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dub ^= i
        if a & differ_bit:
            miss_or_dub ^= a

    return (DuplicateAndMissing(miss_or_dub, miss_or_dub ^ miss_xor_dup)
            if miss_or_dub in A else
            DuplicateAndMissing(miss_or_dub ^ miss_xor_dup, miss_or_dub))

A = [5, 5, 0, 3, 4, 2]
print(duplicate_missing(A))
