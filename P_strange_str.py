# def solution(s):
#     answer = ""
#     for word in s.split():
#         target = ""
#         for index in range(len(word)):
#             if index % 2 == 0:
#                 target += word[index].upper()
#             else:
#                 target += word[index].lower()
#         answer += target + " "

#     return answer[:-1]

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
