def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer



case = solution(123)
print(case)        # 6

case = solution(987)
print(case)        # 24