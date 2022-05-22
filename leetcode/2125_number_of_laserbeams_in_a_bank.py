def numberOfBeams(bank):
    lasers = list(filter(lambda x: x.count('1') > 0, bank))
    return sum(lasers[i].count('1') * lasers[i - 1].count('1') for i in range(1, len(lasers)))

bank = ["011001","000000","010100","001000"]
print(numberOfBeams(bank))
