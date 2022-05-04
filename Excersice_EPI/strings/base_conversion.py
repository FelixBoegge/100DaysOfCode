import functools
import string


def convert_base(s: str, b1: int, b2: int) -> str:
    def construct_from_base(x, base):
        return '' if x == 0 else construct_from_base(x//base, base) + string.hexdigits[x % base].upper()

    is_negative = s[0] == '-'
    x = functools.reduce(lambda y, c: y * b1 + string.hexdigits.index(c.lower()), s[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if x == 0 else construct_from_base(x, b2))

print(convert_base('615', 7, 13))
