# int x의 각 자릿수를 더한 값을 sum이라고 하자.
# x가 sum으로 나누어 떨어지는 경우 x는 하샤드 수이다.
# x가 하샤드 수인지 판별하는 프로그램을 작성하라.
def solution(x):
    target = 0
    for i in str(x):
        target += int(i) 
    return (x % target == 0)


case = solution(10)
print(case)             #true
case = solution(12)
print(case)             #true
case = solution(11)
print(case)             #false
case = solution(13)
print(case)             #false

