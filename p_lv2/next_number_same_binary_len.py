def solution(n):
    target = bin(n).count('1')
    while(True):
        n += 1
        if (bin(n).count('1') == target):
            break
        
    return n



case = solution(78)
print(case)     # 83

case = solution(15)
print(case)     # 23