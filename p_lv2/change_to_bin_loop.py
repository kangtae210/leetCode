


def solution(s):
    loop = 0
    zero = []
    while True:
        if s == "1": 
            break
        zero.append(s.count('0'))
        s = bin(len(s.replace('0',  "")))[2:]
        loop += 1

    return [loop, sum(zero)]





s = "110010101001"
case = solution(s)
print(case)     # [3,8]

s = "01110"
case = solution(s)
print(case)     # [3,3]

s = "1111111"
case = solution(s)
print(case)     # [4,1]