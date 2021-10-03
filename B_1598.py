import sys
import math

first, second = map(int, sys.stdin.readline().split())

f_x = math.ceil(first / 4)
f_y = first % 4
if f_y == 0:
    f_y = 4

s_x = math.ceil(second / 4)
s_y = second % 4
if s_y == 0:
    s_y = 4
    
answer = int(abs(f_x - s_x) + abs(f_y - s_y))

print(answer)