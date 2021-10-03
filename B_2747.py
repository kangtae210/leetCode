import sys

input = int(sys.stdin.readline())


arr = [0,1]



for i in range(input-1):
    x = arr[-1]
    y = arr[-2]

    arr.append(x+y)


print(arr[-1])

