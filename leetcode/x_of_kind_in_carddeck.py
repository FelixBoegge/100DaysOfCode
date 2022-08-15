import collections
from functools import reduce
from fractions import gcd


def hasGroupsSizeX(deck: [int]) -> bool:
    group_sizes = collections.Counter(deck).values()
    return reduce(gcd, group_sizes) >= 2

deck = [1,1,1,2,2,2,3,3]
print(hasGroupsSizeX(deck))
