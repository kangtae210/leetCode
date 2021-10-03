import sys

input = int(sys.stdin.readline())
x = '*'

for i in range(input):
    for j in range(i+1):
        print(x, end="")
    print()
for i in range(input-1,0,-1):
    for j in range(i):
        print(x, end="")
    print()    