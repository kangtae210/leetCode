def solution(d, budget):
    d = sorted(d)
    count = 0
    for i in range(len(d)):
        budget = budget - d[i]
        if budget < 0:
            break
        count += 1
    return count


case = solution([1, 3, 2, 5, 4], 9)
print(case)     # 3

case = solution([2, 2, 3, 3], 10)
print(case)     # 4
