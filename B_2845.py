import sys

people, area = sys.stdin.readline().split()
people = int(people) * int(area)

report = sys.stdin.readline().split()

answer = ""
for i in range(len(report)):
    report[i] = int(report[i]) - people
    answer +=str(report[i]) +" "






print(answer)