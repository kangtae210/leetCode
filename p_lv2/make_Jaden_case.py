def solution(s):
    answer = ''
    move = 0

    for i in range(len(s)):
        if (s[i] == " "):
            answer += " "
            move = 0
            continue
        if (move == 0):
            answer += s[i].upper()
            move += 1
        else:
            answer += s[i].lower()
            move+=1

    return answer




s = "3people unFollowed me"
case = solution(s)
print(case)      # "3people Unfollowed Me"

s = "for the last week"
case = solution(s)
print(case)     # "For The Last Week"