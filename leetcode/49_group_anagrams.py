def groupAnagrams(strs):
    idx = {}
    res = []
    for s in strs:
        sk = "".join(sorted(s))
        if sk in idx:
            res[idx[sk]].append(s)
        else:
            idx[sk] = len(res)
            res.append([s])
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
