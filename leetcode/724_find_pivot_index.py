
def pivotIndex(nums) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

nums = [1,7,3,6,5,6]
nums2 = [-1,-1,-1,-1,0,1]
print(pivotIndex(nums2))

