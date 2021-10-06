# 정수 n을 입력받아 n의 약수를 모두 더한 값을
# 리턴하는 함수 solution을 작성하라.

def solution(n):
    answer = 0
    for i in range(n):
        if n % (i+1) == 0:
            answer = answer + (i+1)
    return answer



case = solution(12) #1,2,3,4,6,12
print(case)         #28
case = solution(5)  #1,5
print(case)         #6