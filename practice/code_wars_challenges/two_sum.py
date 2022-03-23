def two_sum(n, t):
    h = {}
    for i in range(len(n)):
        if t-n[i] in h.keys():
            return [h[t-n[i]], i]
        else:
            h[n[i]] = i

nums = [1,2,3]
target = 4
nums2 = [1234,5678,9012]
target2 = 14690

print(two_sum(nums2, target2))
