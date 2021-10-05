def solution(arr):
    x = min(arr)
    arr.remove(x)
    if len(arr) == 0:
        arr.append(-1)
    return arr


case = solution([4,3,2,1])
print(case)
case = solution([10])
print(case)