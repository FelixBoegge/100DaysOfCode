def addToArrayForm(num: [int], k: int):
    num[-1] += k
    for i in range(len(num) - 1, 0, -1):
        if num[i] < 10:
            return num
        temp = num[i] // 10
        num[i] %= 10
        num[i - 1] += temp
    while num[0] >= 10:
        temp = num[0] // 10
        num[0] %= 10
        num.insert(0, temp)
    return num

num = [1,9,9]
k = 802
print(addToArrayForm(num, k))
