def change_matrix(arr):
    answer = []
    for i in range(len(arr[0])):
        target = []
        for j in range(len(arr)):
            target.append(arr[j][i])
        answer.append(target)
        
    return answer

def multiple_vector(arr1, arr2):
    answer = 0
    for i in range(len(arr1)):
        answer += arr1[i] * arr2[i]
    return answer


def solution(arr1, arr2):
    answer = []
    arr2 = change_matrix(arr2)
    
    for i in range(len(arr1)):
        target = []
        for j in range(len(arr2)):
           x = multiple_vector(arr1[i], arr2[j])
           target.append(x)
        answer.append(target)
        
    return answer



arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]	
case = solution(arr1, arr2)
print(case)
# [[15, 15], [15, 15], [15, 15]]



arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
case = solution(arr1, arr2)
print(case)
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]