def solution(answers):
    person1 = [1, 2, 3, 4, 5]                   # 1번 수포자가 찍는 방식
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]          # 2번 수포자가 찍는 방식
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]    # 3번 수포자가 찍는 방식
    corrects = [0, 0, 0]

    for i in range(len(answers)):
        if (answers[i] == person1[i % len(person1)]):
            corrects[0] += 1
        if (answers[i] == person2[i % len(person2)]):
            corrects[1] += 1
        if (answers[i] == person3[i % len(person3)]):
            corrects[2] += 1        
        
    
    max_correct = max(corrects)
   
    answer = []
    for i in range(3):
        if(max_correct == corrects[i]):
            answer.append(i+1)
        
    
    return answer




print("*****************")
case = solution([1,2,3,4,5])
print(case)     #[1]
print("*****************")
case = solution([1,3,2,4,2])
print(case)     #[1,2,3]
