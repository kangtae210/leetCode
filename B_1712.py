# 고정비용 A, 가변비용 B, 개당 가격 C
import sys
import math
answer = 0
A,B,C = map(int, sys.stdin.readline().split())
if B >= C:
    answer = -1
else:
    answer = math.floor((A / (C - B))) + 1

print(answer)