def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1


    while True:
        if left == right:
            answer += 1
            break
        if left > right:
            break

        if people[left] + people[right] > limit:
            answer += 1
            right -= 1
        else:
            answer += 1
            left += 1
            right -= 1   

    return answer




people = [50, 50, 70, 80]
limit = 100
case = solution(people= people, limit= limit)
print(case)     # 3


people = [70, 80, 50]
limit = 100
case = solution(people= people, limit= limit)
print(case)     # 3

people = [40, 50, 150, 160]
limit = 200
case = solution(people= people, limit= limit)
print(case)     # 2

people = [100, 500, 500, 900, 950]
limit = 1000
case = solution(people= people, limit= limit)
print(case)     # 3

people = [40, 40, 40]
limit = 100
case = solution(people= people, limit= limit)
print(case)     # 2


people = [40, 50, 60, 90]
limit = 100
case = solution(people= people, limit= limit)
print(case)     # 3


people = [40]
limit = 100
case = solution(people= people, limit= limit)
print(case)     # 1





