def solution(s):
    index, move = 0,0
    answer = []
    s = list(s)
    for index in range(len(s)):
        if s[index] == " ":
            answer.append(" ")
            move = 0
            continue
        else:
            move += 1
        
        if move %2 == 0:
            answer.append(s[index].lower())
        else:
            answer.append(s[index].upper())
    answer = "".join(answer)
    return answer



case = solution("try hello world")
print(case)     # TrY HeLlO WoRlD
