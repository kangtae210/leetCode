def solution2(n):
    square_num = 0
    for i in range(n):
        if 2 ** i >= n:
            square_num = i
            break
    idx = n - 2 ** (square_num-1)

    arr = [1]
    for i in range(square_num-1):
        target = []
        for j in range(len(arr)):
            target.append(arr[j] + 1)
        arr += target

    return arr[idx]

def solution(n):
    answer = 0
    while True:
        if n == 0:
            break
        
        if n % 2 == 1:
            n -= 1
            answer += 1
        else:
            n = n // 2
    

    return answer 




case = solution(10)
print(case)     #2

case = solution(6)
print(case)     #2

case = solution(5000)
print(case)     #5

