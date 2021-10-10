def solution(arr):
    answer = ["x"]
    for target in arr:
        if target != answer[-1]:
            answer.append(target)
    return answer[1:]



case = solution([1, 1, 3, 3, 0, 1, 1])
print(case)        #[1, 3, 0, 1]

case = solution([4, 4, 4, 3, 3])
print(case)        #[4, 3]