def solution(numbers):

    return sum(set(range(1, 10)) - set(numbers))




case = solution([1,2,3,4,6,7,8,0])
print(case)     #14

case = solution([5,8,4,0,6,7,9])
print(case)     #6