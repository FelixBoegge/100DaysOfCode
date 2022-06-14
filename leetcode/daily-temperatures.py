def dailyTemperatures(temperatures) -> [int]:
    days = [0] * len(temperatures)
    wait = []
    for i in range(len(temperatures)):
        #days[i] = 1
        wait.append(i)
        for j in wait:
            if temperatures[j] >= temperatures[i]:
                days[j] += 1
            else:
                wait.remove(j)

    for i in wait:
        days[i] = 0

    return days

temps = [73,74,75,71,69,72,76,73]
       #[1,1,4,2,1,1,0,0]
print(dailyTemperatures(temps))
