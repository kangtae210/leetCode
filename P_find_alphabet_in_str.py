def solution(s):
    count = list(s.lower()).count('p') - list(s.lower()).count('y')
    return count==0

case = solution("pPoooyY")
print(case)     #True
case = solution("Pyy")
print(case)     #False