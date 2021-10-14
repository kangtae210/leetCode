def solution(absolutes, signs):
    for i in range(len(absolutes)):
        absolutes[i] = absolutes[i] * (-1) ** [True, False].index(signs[i])

    return sum(absolutes)



case = solution([4,7,12], [True,False,True])
print(case)     # 9

case = solution([1,2,3], [False,False,True])
print(case)     # 0