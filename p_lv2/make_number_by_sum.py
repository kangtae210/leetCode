def solution(n):
    answer = []
    for i in range(n):

        arr = []
        move = 0
        while True:
            arr.append(i+move+1)
            move += 1
            if sum(arr) >= n:
                break
        
        if (sum(arr) == n):
            answer.append(arr)

    return len(answer)




case = solution(15)
print(case)     # 4