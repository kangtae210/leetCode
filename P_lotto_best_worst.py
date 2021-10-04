def solution(lottos, win_nums):
    countZero = 0
    same = 0
    for my in lottos:
        if my == 0:
            countZero += 1

        for your in win_nums:
            if my == your:
                same += 1

    answer = []     # 가능한 최고 등수, 가능한 최저 등수
    
    if same + countZero == 0:       # 최고등수
        answer.append(6)
    else:
        answer.append(7-countZero - same)

    if same == 0:                   # 최저등수
        answer.append(6)
    else:
        answer.append(7-same)

    return answer



lottos = [45, 4, 35, 20, 3, 9]
win_nums = 	[20, 9, 3, 45, 4, 35]	
answer = solution(lottos, win_nums)     #[3,5]

print(answer)