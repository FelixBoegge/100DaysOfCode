def findJudge(n: int, trust) -> int:
    if not trust:
        if n == 1:
            return 1
        else:
            return -1
    trusts = {}
    people_notrust = [i for i in range(1, n + 1)]
    for i in range(len(trust)):
        if trust[i][1] in trusts.keys():
            trusts[trust[i][1]] += 1
        else:
            trusts[trust[i][1]] = 1
        if trust[i][0] in people_notrust:
            people_notrust.remove(trust[i][0])
    for person in people_notrust:
        if person in trusts.keys():
            if trusts[person] == n - 1:
                return person
    return -1

n = 11
trust = [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
print(findJudge(n, trust))
