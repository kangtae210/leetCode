def make_fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return make_fibo(n-1) + make_fibo
    


def solution2(n):
    return make_fibo(n) % 1234567

def solution(n):
    fibos = [0,1]
    for i in range(n-1):
        fibos.append(fibos[-1] + fibos[-2])
    return fibos[-1] % 1234567

case = solution(3)
print(case) # 2

case = solution(5)
print(case) # 5