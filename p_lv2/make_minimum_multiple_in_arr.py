def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer




arr1 = [1, 4, 2]
arr2 = [5, 4, 4]
case = solution(arr1, arr2)
print(case)     #29

arr1 = [1, 2]
arr2 = [3, 4]
case = solution(arr1, arr2)
print(case)     #10