# 콜라츠 추측
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2  . 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

# 위 작업을 얼마나 반복해야하는지를 반환하는 함수 solution()을 작성하라.
# 단, 작업을 500번 반복해도 1이 되지 않는다면 -1을 반환한다.
def solution(num):
    for i in range(500):
        if num == 1:
            return i

        if num %2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        
    return -1


case = solution(6)
print(case)
case = solution(16)
print(case)
case = solution(626331)
print(case)