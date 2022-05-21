def romanToInt(s: str) -> int:
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = val[s[0]]
    for i in range(1, len(s)):
        if val[s[i]] > val[s[i - 1]]:
            num += (val[s[i]] - 2 * (val[s[i - 1]]))
        else:
            num += val[s[i]]
    return num

roman = "MCMXCIV"
print(romanToInt(roman))
