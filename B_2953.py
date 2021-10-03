import sys

class person:
    def __init__(self, arr) -> None:
        self.scores = arr
    def sum(self):
        sum = 0
        for i in self.scores:
            sum += int(i)
        
        return sum

people = []


for i in range(5):
    x = sys.stdin.readline().split()
    people.append(person(x).sum())

max_index = people.index(max(people)) + 1
max_val = max(people)

print(max_index, max_val)
