import numpy as np
# 두 수를 입력받아 최대공약수와 최소공배수를
# 배열로 받아 반환하는 함수 solution()을 작성하라.
def solution(n, m):
    answer = []
    x = gcd(n,m)
    answer.append(x)
    answer.append(int(n * m / x))

    return answer

def gcd(a,b):
    if a<b:
        temp = a
        a = b
        b = temp
    
    r = a % b
    print(a, "=", b, "X", int(a/b),'+', r)

    if r==0:
        return b
    else:
        return gcd(b,r)



case = solution(3,12)
print(case)     #[3,12]
case = solution(2,5)
print(case)     #[1,10]

x = gcd(120,36)
print(x)