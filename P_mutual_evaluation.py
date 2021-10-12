def grade(num):
    if num>=90:
        return 'A'
    elif 80 <=num < 90:
        return 'B'
    elif 70 <=num < 80:
        return 'C'
    elif 50 <=num < 70:
        return 'D'
    else:
        return 'F'

def avg(arr):
    return sum(arr) / len(arr)

def solution(scores):
    answer = ""

    for student in range(len(scores)):
        one = []
        for i in range(len(scores)):
            one.append(scores[i][student])
        
        if one[student] == min(one) or one[student] == max(one):
            if one.count(one[student]) == 1:
                del(one[student]) 
        
        target = avg(one)
        answer += grade(target)
        

    return answer




scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
case = solution(scores)
print(case)     #"FBABD"

scores = [[50,90],[50,87]]
case = solution(scores)
print(case)     #"DA"

scores = [[70,49,90],[68,50,38],[73,31,100]]
case = solution(scores)
print(case)     #"CFD"