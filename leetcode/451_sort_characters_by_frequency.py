def frequencySort(s: str) -> str:
    count = {}
    out = ""
    for c in s:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    freq = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for key, value in freq.items():
        out += value * key
    return out

s = 'treett'
print(frequencySort(s))
