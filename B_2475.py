import sys
str = sys.stdin.readline().split()

stdnum = 0

for i in str:
    stdnum += int(i) * int(i)

stdnum = stdnum % 10
print(stdnum)