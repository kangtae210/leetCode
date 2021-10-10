def solution(a, b):
    answer = 0
    for i in range(min(a,b), max(a,b)+1):
        answer += i
    return answer


def solution2(a, b):
    return sum(range(min(a,b), max(a,b)+1))


case = solution2(3, 5)
print(case)     #12

case = solution2(3, 3)
print(case)     #3

case = solution2(5, 3)
print(case)     #12