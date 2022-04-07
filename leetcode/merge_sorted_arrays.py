def merge(nums1, m, nums2, n) -> None:
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return
    if n == 0:
        return
    pointer1 = 0
    pointer2 = 0
    while pointer1 < m + n and pointer2 < n:
        if pointer1 == m+1:
            nums1[pointer1:] = nums2[pointer2:]
            break
        if nums1[pointer1] > nums2[pointer2]:
            nums1.insert(pointer1, nums2[pointer2])
            nums1.pop()
            pointer1 += 1
            pointer2 += 1
        else:
            pointer1 += 1


A = [-1,-1,0,0,0,0]
m = 4
B = [-1,0]
n = 2
merge(A,m,B,n)
print(A)