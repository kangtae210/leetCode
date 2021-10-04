#x부터 x씩 증가하는 n개의 원소를 가진 배열을 반환하는 프로그램
def solution(x, n):     
    answer = []
    for i in range(n):
        answer.append(x* (i+1))
    return answer

