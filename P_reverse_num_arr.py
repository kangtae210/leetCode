def solution(n):
    answer = []
    for i in str(n):
        answer.insert(0,int(i))
    return answer



case = solution(12345)
print(case)     #54321