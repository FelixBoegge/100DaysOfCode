def queue_time(c, n):
    tills = []
    time = 0
    for i in range(n):
        if c:
            tills.append(c.pop(0))
    while sum(tills) > 0:
        tills = [x-1 for x in tills if x>0]
        time += 1
        for i in range(len(tills)):
            if tills[i] == 0:
                if c:
                    tills[i] = c.pop(0)
    return time

c = [1,2,3,4,5]
n = 3
print(queue_time(c, n))
