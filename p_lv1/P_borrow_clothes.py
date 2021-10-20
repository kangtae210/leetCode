def solution(n, lost, reserve): # 전체 학생수, 잃어버린 학생 수, 여벌옷이 있는 학생 수

    # 여벌 옷이 있는 학생이 체육복을 도난당한 경우
    for i in range(1, n+1):
        if ((i in lost) and (i in reserve)):
            lost.remove(i)
            reserve.remove(i)
    
    
    for i in range(1, n+1):
        if i in lost :
            if (i - 1) in reserve :
                reserve.remove(i - 1)
                lost.remove(i)
            elif (i + 1) in reserve :
                reserve.remove(i + 1)
                lost.remove(i)
        



    return n - len(lost)
    # 체육 수업을 들을 수 있는 최대 학생수



case = solution(5, [2, 4], [1, 3, 5])
print(case)     #5

print("********************")

case = solution(5, [2, 4], [3])
print(case)     #4

print("********************")

case = solution(3, [3], [1])
print(case)     #2

print("********************")

case = solution(5, [1,2,3], [2,3,4])
print(case)     #4


print("********************")

case = solution(10, [5,4,3,2,1], [3,1,2,5,4])
print(case)     #10