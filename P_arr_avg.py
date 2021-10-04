import numpy as np

def solution(arr):
    
    answer = np.average(arr)
    return answer




x = solution([1,2,3,4])
print(x)                #2.5

x = solution([5,5])
print(x)                #5
