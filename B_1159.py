import sys

people = int(sys.stdin.readline())

firsts = []
counts = []
for i in range(people):
    name = sys.stdin.readline()
    if name[0] in firsts:
        counts[firsts.index(name[0])] += 1
    else:
        firsts.append(name[0])
        counts.append(1)

answer = []
for i in range(len(counts)):
    if counts[i]>= 5:
        answer.append(firsts[i])

answer.sort()

str = ""
if answer == []:
    str = 'PREDAJA'
else:
    for i in answer:
        str += i

print(str)