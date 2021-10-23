
def solution(s):
    arr = [-1]
    for i in s:
        if i == "(":
            arr.append("(")
        else:
            if arr.pop() != "(":
                break
    
    return len(arr) == 1






case = solution("()()")
print(case)     # true

case = solution("(())()")
print(case)     # true

case = solution(")()(")
print(case)     # false

case = solution("(()(")
print(case)     # false