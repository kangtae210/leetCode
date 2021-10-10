def solution(n):
    answer = "수박" * int(n/2) + "수" * (n%2)
    return answer


case = solution(3)
print(case)     #수박수
case = solution(4)
print(case)     #수박수박