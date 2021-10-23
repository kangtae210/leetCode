def solution(s):
    
    arr = sorted(list(map(int, s.split())))
    
    return str(arr[0]) + " " + str(arr[-1])



s = "1 2 3 4"
case = solution(s)
print(case)     #"1 4"

s = "-1 -2 -3 -4"
case = solution(s)
print(case)     #"-4 -1"

s = "-1 -1"
case = solution(s)
print(case)     #"-1 -1"



