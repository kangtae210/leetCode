def solution(N, stages): 
    
    ratios = [[0,0,0.0, i+1] for i in range(N)]

    fight = 0
    for i in range(1, N+1):
        fail = stages.count(N-i+1)
        fight += fail
        ratios[N-i][0] += fail
        ratios[N-i][1] += fight
        pass
    
    finish = stages.count(N+1)
    for i in ratios:
        i[1] += finish
        if i[1] !=0:
            i[2] = i[0] / i[1]
        else:
            i[2] = 0.0
    

    ratios.sort(key= lambda x : -x[2])

    answer = []
    for i in range(N):
        answer.append(ratios[i][3])
    return answer

print("**********************************")
case = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(case)     #[3,4,2,1,5]

print("**********************************")
case = solution(4, [4, 4, 4, 4, 4])
print(case)     #[4,1,2,3]