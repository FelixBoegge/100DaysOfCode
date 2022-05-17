import functools


def roman_to_decimal(s: str) -> int:
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    return functools.reduce(
        lambda val, i: val + (-value[s[i]] if  value[s[i]] < value[s[i+1]] else value[s[i]]), reversed(range(len(s)-1)), value[s[-1]]
    )

rome = 'DMMXXII'
print(roman_to_decimal(rome))
