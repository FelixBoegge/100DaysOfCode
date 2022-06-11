def timeRequiredToBuy(tickets, k):
    count = 0
    pos = k
    tickets_to_buy = tickets[pos]
    while tickets_to_buy > 0:
        tickets[0] -= 1
        tmp = tickets.pop(0)
        count += 1
        pos -= 1
        if tmp > 0:
            tickets.append(tmp)
        if pos == -1:
            tickets_to_buy -= 1
            pos = len(tickets) - 1
    return count

tickets = [2,3,4,1,2]
k = 1
print(timeRequiredToBuy(tickets, k))
