# factorial 진법
import sys

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)


def solution(str):
    ret_val = 0

    length = len(str)
    for i in range(length):
        ret_val += int(str[i]) * factorial(length - i)
    
    return ret_val

cases = []
while True:
    input_str = int(sys.stdin.readline())
    if input_str == 0:
        break
    x = solution(str(input_str))
    cases.append(x)

for i in cases:
    print(i)

    
