import csv


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]


t = HashTable()
l = []

with open('temperature.csv', mode='r') as file:
    days = csv.reader(file, delimiter=',')
    next(days)
    for day in days:
        t[day[0]] = int(day[1])
        l.append(int(day[1]))

for i in range(len(t.arr)):
    print(t.arr[i])

print(l)
print(f"Average Temperature in first week was : {sum(l[0:7])/7}")
print(f"Maximum Temperature was : {max(l[:10])}")

print(f"Temperature on Jan 9 was: {t['Jan 9']}")
print(f"Temperature on Jan 4 was: {t['Jan 4']}")
