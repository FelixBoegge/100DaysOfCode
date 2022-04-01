def buy_sell_stock(sp):
    current_min = sp[0]
    max = 0
    current_lowest = [current_min]
    for i in range(1, len(sp)):
        if sp[i] < current_min:
            current_lowest.append(sp[i])
            current_min = sp[i]
        else:
            current_lowest.append(current_min)
    for i in range(len(current_lowest)):
        if sp[i] - current_lowest[i] > max:
            max = sp[i] - current_lowest[i]
    return max if max > 0 else "no profit possible"

prices = [310,315,275,295,260,270,290,230,255,250]
prices2 = [230, 220, 180, 150, 100]
print(buy_sell_stock(prices2))
