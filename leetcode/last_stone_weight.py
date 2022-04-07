def lastStoneWeight(stones) -> int:
    stones.sort()
    while stones:
        y = stones.pop()
        if not stones:
            return y
        x = stones.pop()
        if y > x:
            y -= x
            for i in range(len(stones) + 1):
                if i == len(stones) or y <= stones[i]:
                    stones.insert(i, y)
                    break
    return 0

stones = [3,7,8]
print(lastStoneWeight(stones))