def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.update([numbers[i] + numbers[j]])
            
    return sorted(list(answer))




case = solution([2,1,3,4,1])
print(case)     #[2,3,4,5,6,7]

case = solution([5,0,2,7])
print(case)	    #[2,5,7,9,12]