def shipWithinDays(weights: [int], days: int) -> int:
    def capacity(capacity):
        next_weight = 0
        for day in range(days):
            day_cargo = 0
            while next_weight < len(weights) and day_cargo + weights[next_weight] <= capacity:
                day_cargo += weights[next_weight]
                next_weight += 1
        if next_weight < len(weights):
            return False
        return True

    res = None
    left, right = max(weights), (max(weights) * 2) * (len(weights) // days)
    while left <= right:
        pivot = left + (right - left) // 2
        if capacity(pivot):
            res = pivot
            right = pivot - 1
        else:
            left = pivot + 1
    return res


weights = [10,50,100,100,50,100,100,100]
day = 5
print(shipWithinDays(weights, day))
