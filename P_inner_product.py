# 내적 : a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer




case = solution([1,2,3,4], [-3,-1,0,2])
print(case)     # 3

case = solution([-1,0,1], [1,0,-1])
print(case)     # -2