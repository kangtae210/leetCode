def solution(left, right):
    check_odd_factor = 0
    for target in range(left, right+1):
        num = pow(target, 0.5)
        if num == int(num):
            check_odd_factor += target

    return sum(range(left, right+1))- 2 * check_odd_factor










case = solution(13,17)
print(case)     # 43

case = solution(24, 27)
print(case)     # 52
