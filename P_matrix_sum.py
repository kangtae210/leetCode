def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        target = []
        for j in range(len(arr1[0])):
            target.append(arr1[i][j]+ arr2[i][j])
        answer.append(target)
    return answer



arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
x = solution(arr1, arr2)        #[[4,6],[7,9]]
print(x)

arr1 = [[1],[2]]
arr2 = [[3],[4]]
x = solution(arr1, arr2)        #[[4],[6]]
print(x)