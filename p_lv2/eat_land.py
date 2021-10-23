def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            target_list = land[i-1][0 : j] + land[i-1][j+1 : 4]
            land[i][j] += max(target_list)
    
    return max(land[-1])

land = [
    [1, 1, 1, 1],
    [2, 2, 2, 3],
    [3, 3, 3, 6],
    [4, 4, 4, 7]
]	
case = solution(land)
print(case)     # 