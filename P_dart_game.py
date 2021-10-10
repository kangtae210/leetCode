def solution(dartResult):
    scores = []
    for i in range(len(dartResult)):
        check_ten = (dartResult[i] == '1' and dartResult[i+1] == '0')
        check_ten_second = (dartResult[i-1] == '1' and dartResult[i] == '0')
        if check_ten:
            scores.append(10)
        elif '0' <= dartResult[i] <= '9' and not(check_ten_second):
            scores.append(int(dartResult[i]))
        
        if dartResult[i] == 'D':
            scores[-1] = scores[-1] ** 2
        elif dartResult[i] == 'T':
            scores[-1] = scores[-1] ** 3
        
        if dartResult[i] == '*':
            scores[-1] = scores[-1] * 2
            try:
                scores[-2] = scores[-2] * 2
            except:
                pass
        
        elif dartResult[i] == '#':
            scores[-1] = scores[-1] * (-1)
    return sum(scores)


# 1
case = solution("1S2D*3T") 
print(case)     #37
# 2
case = solution("1D2S#10S")
print(case)     #9
# 3
case = solution("1D2S0T")
print(case)     #3
# 4
case = solution("1S*2T*3S")
print(case)     #23
# 5
case = solution("1D#2S*3S")
print(case)     #5
# 6
case = solution("1T2D3D#")
print(case)     #-4
# 7
case = solution("1D2S3T*")
print(case)     #59


